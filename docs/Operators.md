# Operator Schemas

Operators are a collection of basic processes that assist in data modification, cleaning, filtering, deduplication, etc. We support a wide range of data sources and file formats, and allow for flexible extension to custom datasets.


## Overview

The operators in Data-Juicer are categorized into 5 types.

| Type                              | Number | Description |
|-----------------------------------|:------:|-------------|
| [ Formatter ]( #formatter )       |    7   | Discovers, loads, and canonicalizes source data |
| [ Mapper ]( #mapper )             |   17   | Edits and transforms samples                    |
| [ Filter ]( #filter )             |   15   | Filters out low-quality samples                 |
| [ Deduplicator ]( #deduplicator ) |    3   | Detects and removes duplicate samples           |
| [ Selector ]( #selector )         |    2   | Selects top samples based on ranking            |


All the specific operators are listed below, each featured with several capability tags.

* Domain Tags
    - General: general purpose
    - LaTeX: specific to LaTeX source files
    - Code: specific to programming codes
    - Financial: closely related to financial sector
* Language Tags
    - en: English
    - zh: Chinese


## Formatter <a name="formatter"/>

| Operator          | Domain  |  Lang  | Description                                                        |
|-------------------|---------|--------|--------------------------------------------------------------------|
| remote_formatter  | General | en, zh | Prepares datasets from remote (e.g., HuggingFace)                  |
| csv_formatter     | General | en, zh | Prepares local `.csv` files                                        |
| tsv_formatter     | General | en, zh | Prepares local `.tsv` files                                        |
| json_formatter    | General | en, zh | Prepares local `.json`, `.jsonl`, `.jsonl.zst` files               |
| parquet_formatter | General | en, zh | Prepares local `.parquet` files                                    |
| text_formatter    | General | en, zh | Prepares other local text files ([complete list](../data_juicer/format/text_formatter.py#L63,73)) |
| mixture_formatter | General | en, zh | Handles a mixture of all the supported local file types           | 


## Mapper <a name="mapper"/>

| Operator                                      | Domain             | Lang   | Description                                                                                                    |
|-----------------------------------------------|--------------------|--------|----------------------------------------------------------------------------------------------------------------|
| remove_header_mapper                          | LaTeX              | en, zh | Removes the running headers of TeX documents, e.g., titles, chapter or section numbers/names                   |
| remove_bibliography_mapper                    | LaTeX              | en, zh | Removes the bibliography of TeX documents                                                                      |
| expand_macro_mapper                           | LaTeX              | en, zh | Expands macros usually defined at the top of TeX documents                                                     |
| whitespace_normalization_mapper               | General            | en, zh | Normalizes various Unicode whitespaces to the normal ASCII space (U+0020)                                      |
| punctuation_normalization_mapper              | General            | en, zh | Normalizes various Unicode punctuations to their ASCII equivalents                                             |
| fix_unicode_mapper                            | General            | en, zh | Fixes broken Unicodes (by [ftfy](https://ftfy.readthedocs.io/))                                        |
| sentence_split_mapper                         | General            | en     | Splits and reorganizes sentences according to semantics                                                        |
| remove_long_words_mapper                      | General            | en, zh | Removes words with length outside the specified range                                                       |
| remove_words_with_incorrect_<br />substrings_mapper | General            | en, zh | Removes words containing specified substrings                                                                  |
| clean_email_mapper                            | General            | en, zh | Removes email information                                                                                      |
| clean_ip_mapper                               | General            | en, zh | Removes IP addresses                                                                                           |
| clean_links_mapper                            | General, Code      | en, zh | Removes links, such as those starting with http or ftp                                                         |
| clean_html_mapper                             | General            | en, zh | Removes HTML tags and returns plain text of all the nodes                                                      |
| remove_table_text_mapper                      | General, Financial | en     | Detects and removes possible table contents (:warning: relies on regular expression matching and thus fragile) |
| clean_copyright_mapper                        | Code               | en, zh | Removes copyright notice at the beginning of code files (:warning: must contain the word *copyright*)        |
| remove_specific_chars_mapper                  | General            | en, zh | Removes any user-specified characters or substrings                                                            |


## Filter <a name="filter"/>

| Operator                       | Domain  | Lang   | Description                                                                                |
|--------------------------------|---------|--------|--------------------------------------------------------------------------------------------|
| word_num_filter                | General | en, zh | Keeps samples with word count within the specified range                                   |
| stopwords_filter               | General | en, zh | Keeps samples with stopword ratio above the specified threshold                            |
| flagged_words_filter           | General | en, zh | Keeps samples with flagged-word ratio below the specified threshold                        |
| character_repetition_filter    | General | en, zh | Keeps samples with char-level n-gram repetition ratio within the specified range           |
| word_repetition_filter         | General | en, zh | Keeps samples with word-level n-gram repetition ratio within the specified range           |
| special_characters_filter      | General | en, zh | Keeps samples with special-char ratio within the specified range                           |
| language_id_score_filter       | General | en, zh | Keeps samples of the specified language, judged by a predicted confidence score            |
| perplexity_filter              | General | en, zh | Keeps samples with perplexity score below the specified threshold                          |
| maximum_line_length_filter     | Code    | en, zh | Keeps samples with maximum line length within the specified range                          |
| average_line_length_filter     | Code    | en, zh | Keeps samples with average line length within the specified range                          |
| alphanumeric_filter            | General | en, zh | Keeps samples with alphanumeric ratio within the specified range                           |
| text_length_filter             | General | en, zh | Keeps samples with total text length within the specified range                            |
| suffix_filter                  | General | en, zh | Keeps samples with specified suffixes                                                      |
| specified_field_filter         | General | en, zh | Filters samples based on field, with value lies in the specified targets                   |
| specified_numeric_field_filter | General | en, zh | Filters samples based on field, with value lies in the specified range (for numeric types) |


## Deduplicator <a name="deduplicator"/>

| Operator                      | Domain  | Lang   | Description                                                 |
|-------------------------------|---------|--------|-------------------------------------------------------------|
| document_deduplicator         | General | en, zh | Deduplicate samples at document-level by comparing MD5 hash |
| document_minhash_deduplicator | General | en, zh | Deduplicate samples at document-level using MinHashLSH      |
| document_simhash_deduplicator | General | en, zh | Deduplicate samples at document-level using SimHash         |


## Selector <a name="selector"/>

| Operator                           | Domain  | Lang   | Description                                                           |
|------------------------------------|---------|--------|-----------------------------------------------------------------------|
| topk_specified_field_selector      | General | en, zh | Selects top samples by comparing the values of the specified field    |
| frequency_specified_field_selector | General | en, zh | Selects top samples by comparing the frequency of the specified field |


## Contributing
We welcome contributions of adding new operators. Please refer to [How-to Guide for Developers](DeveloperGuide.md).
