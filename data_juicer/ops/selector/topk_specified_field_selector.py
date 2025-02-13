import heapq
import sys

from jsonargparse.typing import ClosedUnitInterval, PositiveInt

from ..base_op import OPERATORS, Selector


def to_number(s, reverse=True):
    try:
        return float(s)
    except Exception:
        if reverse:
            return -sys.maxsize
        else:
            return sys.maxsize


@OPERATORS.register_module('topk_specified_field_selector')
class TopkSpecifiedFieldSelector(Selector):
    """Selector to select top samples based on the sorted specified field
    value."""

    def __init__(self,
                 text_key: str = '',
                 top_ratio: ClosedUnitInterval = None,
                 topk: PositiveInt = None,
                 reverse: bool = True,
                 *args,
                 **kwargs):
        """
        Initialization method.

        :param text_key: Selector based on the specified value
            corresponding to the target key. The target key
            corresponding to multi-level field information need to be
            separated by '.'.
        :param top_ratio: Ratio of selected top samples, samples will be
            selected if their specified field values are within this
            parameter. When both topk and top_ratio are set, the value
            corresponding to the smaller number of samples will be
            applied.
        :param topk: Number of selected top sample, samples will be
            selected if their specified field values are within this
            parameter. When both topk and top_ratio are set, the value
            corresponding to the smaller number of samples will be
            applied.
        :param reverse: Determine the sorting rule, if reverse=True,
            then sort in descending order.
        :param args: extra args
        :param kwargs: extra args
        """
        super().__init__(*args, **kwargs)
        self.text_key = text_key
        self.top_ratio = top_ratio
        self.topk = topk
        self.reverse = reverse

    def process(self, dataset):
        if len(dataset) <= 1 or not self.text_key:
            return dataset

        select_num = 0
        if not self.top_ratio:
            if not self.topk:
                return dataset
            else:
                select_num = self.topk
        else:
            select_num = self.top_ratio * len(dataset)
            if self.topk and self.topk < select_num:
                select_num = self.topk

        text_keys = self.text_key.split('.')
        assert text_keys[0] in dataset.features.keys(
        ), "'{}' not in {}".format(text_keys[0], dataset.features.keys())

        if len(text_keys) == 1:
            field_value_list = dataset[text_keys[0]]
        else:
            field_value_list = []
            for item in dataset[text_keys[0]]:
                field_value = item
                for key in text_keys[1:]:
                    assert key in field_value.keys(), "'{}' not in {}".format(
                        key, field_value.keys())
                    field_value = field_value[key]
                field_value_list.append(to_number(field_value, self.reverse))

        if self.reverse:
            select_index = heapq.nlargest(int(select_num), range(len(dataset)),
                                          field_value_list.__getitem__)
        else:
            select_index = heapq.nsmallest(int(select_num),
                                           range(len(dataset)),
                                           field_value_list.__getitem__)
        return dataset.select(select_index)
