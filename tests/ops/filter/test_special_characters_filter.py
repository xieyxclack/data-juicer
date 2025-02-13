import unittest

from datasets import Dataset

from data_juicer.ops.filter.special_characters_filter import \
    SpecialCharactersFilter


class SpecialCharactersFilterTest(unittest.TestCase):

    def _run_special_characters_filter(self, dataset: Dataset, target_list,
                                       op):
        if 'stats' not in dataset.features:
            # TODO:
            # this is a temp solution,
            # only add stats when calling filter op
            dataset = dataset.add_column(name='stats',
                                         column=[{}] * dataset.num_rows)
        dataset = dataset.map(op.compute_stats)
        dataset = dataset.filter(op.process)
        dataset = dataset.select_columns(column_names=['text'])
        res_list = dataset.to_list()
        self.assertEqual(res_list, target_list)

    def test_case(self):

        ds_list = [{
            'text': "Today is Sunday and it's a happy day!"
        }, {
            'text':
            "Today is Sund Sund Sund Sund Sunda and it's a happy day!"
        }, {
            'text': 'a v s e c s f e f g a qkc'
        }, {
            'text': '，。、„”“«»１」「《》´∶：？！（）；–—．～’…━〈〉【】％►'
        }, {
            'text': 'Do you need a cup of coffee?'
        }, {
            'text': 'emoji表情测试下😊，😸31231'
        }]
        tgt_list = [{
            'text': "Today is Sunday and it's a happy day!"
        }, {
            'text':
            "Today is Sund Sund Sund Sund Sunda and it's a happy day!"
        }, {
            'text': 'Do you need a cup of coffee?'
        }]
        dataset = Dataset.from_list(ds_list)
        op = SpecialCharactersFilter(min_ratio=0.0, max_ratio=0.25)
        self._run_special_characters_filter(dataset, tgt_list, op)


if __name__ == '__main__':
    unittest.main()
