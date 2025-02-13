English | [**中文**](README_ZH.md) 

# Data-Juicer: A Data-Centric Text Processing System for Large Language Models

![Data-Juicer](docs/imgs/data-juicer.jpg "Data-Juicer")

![](https://img.shields.io/badge/language-Python-214870.svg)
![](https://img.shields.io/badge/license-Apache--2.0-000000.svg)
[![Contributing](https://img.shields.io/badge/Contribution-welcome-brightgreen.svg)](docs/DeveloperGuide.md)

[![Document_List](https://img.shields.io/badge/Docs-English-blue?logo=Markdown)](README.md#documentation)
[![文档列表](https://img.shields.io/badge/文档-中文-blue?logo=Markdown)](README_ZH.md#documentation)
[![API Reference](https://img.shields.io/badge/Docs-API_Reference-blue?logo=Markdown)](https://alibaba.github.io/data-juicer/)
[![ModelScope-10+ Demos](https://img.shields.io/badge/ModelScope-10+_Demos-4e29ff.svg?logo=data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjI0IDEyMS4zMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIGQ9Im0wIDQ3Ljg0aDI1LjY1djI1LjY1aC0yNS42NXoiIGZpbGw9IiM2MjRhZmYiIC8+Cgk8cGF0aCBkPSJtOTkuMTQgNzMuNDloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzYyNGFmZiIgLz4KCTxwYXRoIGQ9Im0xNzYuMDkgOTkuMTRoLTI1LjY1djIyLjE5aDQ3Ljg0di00Ny44NGgtMjIuMTl6IiBmaWxsPSIjNjI0YWZmIiAvPgoJPHBhdGggZD0ibTEyNC43OSA0Ny44NGgyNS42NXYyNS42NWgtMjUuNjV6IiBmaWxsPSIjMzZjZmQxIiAvPgoJPHBhdGggZD0ibTAgMjIuMTloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzM2Y2ZkMSIgLz4KCTxwYXRoIGQ9Im0xOTguMjggNDcuODRoMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzYyNGFmZiIgLz4KCTxwYXRoIGQ9Im0xOTguMjggMjIuMTloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzM2Y2ZkMSIgLz4KCTxwYXRoIGQ9Im0xNTAuNDQgMHYyMi4xOWgyNS42NXYyNS42NWgyMi4xOXYtNDcuODR6IiBmaWxsPSIjNjI0YWZmIiAvPgoJPHBhdGggZD0ibTczLjQ5IDQ3Ljg0aDI1LjY1djI1LjY1aC0yNS42NXoiIGZpbGw9IiMzNmNmZDEiIC8+Cgk8cGF0aCBkPSJtNDcuODQgMjIuMTloMjUuNjV2LTIyLjE5aC00Ny44NHY0Ny44NGgyMi4xOXoiIGZpbGw9IiM2MjRhZmYiIC8+Cgk8cGF0aCBkPSJtNDcuODQgNzMuNDloLTIyLjE5djQ3Ljg0aDQ3Ljg0di0yMi4xOWgtMjUuNjV6IiBmaWxsPSIjNjI0YWZmIiAvPgo8L3N2Zz4K)](#demos)
[![ModelScope-20+_Refined_Datasets](https://img.shields.io/badge/ModelScope-20+_Refined_Datasets-4e29ff.svg?logo=data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjI0IDEyMS4zMyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIGQ9Im0wIDQ3Ljg0aDI1LjY1djI1LjY1aC0yNS42NXoiIGZpbGw9IiM2MjRhZmYiIC8+Cgk8cGF0aCBkPSJtOTkuMTQgNzMuNDloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzYyNGFmZiIgLz4KCTxwYXRoIGQ9Im0xNzYuMDkgOTkuMTRoLTI1LjY1djIyLjE5aDQ3Ljg0di00Ny44NGgtMjIuMTl6IiBmaWxsPSIjNjI0YWZmIiAvPgoJPHBhdGggZD0ibTEyNC43OSA0Ny44NGgyNS42NXYyNS42NWgtMjUuNjV6IiBmaWxsPSIjMzZjZmQxIiAvPgoJPHBhdGggZD0ibTAgMjIuMTloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzM2Y2ZkMSIgLz4KCTxwYXRoIGQ9Im0xOTguMjggNDcuODRoMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzYyNGFmZiIgLz4KCTxwYXRoIGQ9Im0xOTguMjggMjIuMTloMjUuNjV2MjUuNjVoLTI1LjY1eiIgZmlsbD0iIzM2Y2ZkMSIgLz4KCTxwYXRoIGQ9Im0xNTAuNDQgMHYyMi4xOWgyNS42NXYyNS42NWgyMi4xOXYtNDcuODR6IiBmaWxsPSIjNjI0YWZmIiAvPgoJPHBhdGggZD0ibTczLjQ5IDQ3Ljg0aDI1LjY1djI1LjY1aC0yNS42NXoiIGZpbGw9IiMzNmNmZDEiIC8+Cgk8cGF0aCBkPSJtNDcuODQgMjIuMTloMjUuNjV2LTIyLjE5aC00Ny44NHY0Ny44NGgyMi4xOXoiIGZpbGw9IiM2MjRhZmYiIC8+Cgk8cGF0aCBkPSJtNDcuODQgNzMuNDloLTIyLjE5djQ3Ljg0aDQ3Ljg0di0yMi4xOWgtMjUuNjV6IiBmaWxsPSIjNjI0YWZmIiAvPgo8L3N2Zz4K)](https://modelscope.cn/datasets?organization=Data-Juicer&page=1)

[![QualityClassifier](https://img.shields.io/badge/Tools-Quality_Classifier-saddlebrown?logo=Markdown)](tools/quality_classifier/README.md)
[![AutoEvaluation](https://img.shields.io/badge/Tools-Auto_Evaluation-saddlebrown?logo=Markdown)](tools/evaluator/README.md)

Data-Juicer is a data-centric text processing system to make data higher-quality, juicier, and more digestible for LLMs.
This project is being actively updated and maintained, and we will periodically enhance and add more features and data recipes. We welcome you to join us in promoting LLM data development and research!

----

Table of Contents
=================

* [Data-Juicer: A Data-Centric Text Processing System for Large Language Models](#data-juicer-a-data-centric-text-processing-system-for-large-language-models)
* [Table of Contents](#table-of-contents)
   * [Features](#features)
   * [Prerequisites](#prerequisites)
   * [Installation](#installation)
   * [Quick Start](#quick-start)
      * [Data Processing](#data-processing)
      * [Data Analysis](#data-analysis)
      * [Data Visualization](#data-visualization)
      * [Build Up Config Files](#build-up-config-files)
      * [Preprocess raw data (Optional)](#preprocess-raw-data-optional)
   * [Documentation | 文档](#documentation)
   * [Data Recipes](#data-recipes)
   * [Demos](#demos)
   * [License](#license)
   * [Contributing](#contributing)
   * [References](#references)

## Features

- **Broad Range of Operators**: Equipped with 50+ core [operators (OPs)](docs/Operators.md), including Formatters, Mappers, Filters, Deduplicators, and beyond.

- **Specialized Toolkits**: Feature-rich specialized toolkits such as [Text Quality Classifier](tools/quality_classifier/README.md), [Dataset Splitter](tools/preprocess/README.md), [Analysers](#data-analysis), [Evaluators](tools/evaluator/README.md), and more that elevate your dataset handling capabilities.

- **Systematic & Reusable**: Empowering users with a systematic library of reusable [config recipes](configs) and [OPs](docs/Operators.md), designed to function independently of specific datasets, models, or tasks.

- **Data-in-the-loop**: Allowing detailed data analyses with an automated report generation feature for a deeper understanding of your dataset. Coupled with real-time multi-dimension automatic evaluation capabilities, it supports a feedback loop at multiple stages in the LLM development process.

- **Comprehensive Processing Recipes**: Offering tens of [pre-built data processing recipes](configs/refine_recipe/README.md) for pre-training, SFT, en, zh, and more scenarios.

- **User-Friendly Experience**: Designed for simplicity, with [comprehensive documentation](#documentation), [easy start guides](#quick-start) and [demo configs](configs/README.md), and intuitive configuration with simple adding/removing OPs from [existing configs](configs/config_all.yaml).

- **Flexible & Extensible**: Accommodating most types of data formats (e.g., jsonl, parquet, csv, ...) and allowing flexible combinations of OPs. Feel free to [implement your own OPs](docs/DeveloperGuide.md#build-your-own-ops) for customizable data processing.

- **Enhanced Efficiency**: Providing a speedy data processing pipeline requiring less memory, optimized for maximum productivity.

## Prerequisites

- Recommend Python==3.8
- gcc >= 5 (at least C++14 support)

## Installation

- Run the following commands to install the latest `data_juicer` version in
  editable mode:
```shell
cd <path_to_data_juicer>
pip install -v -e .[all]
```

- Or install optional dependencies:
```shell
cd <path_to_data_juicer>
pip install -v -e .  # install a minimal dependencies
pip install -v -e .[tools] # install a subset of tools dependencies
```

The dependency options are listed below:

| Tag      | Description                                                            |
|----------|------------------------------------------------------------------------|
| .        | Install minimal dependencies for basic Data-Juicer.                    |
| .[all]   | Install all optional dependencies (all of the following)               |
| .[dev]   | Install dependencies for developing the package as contributors        |
| .[tools] | Install dependencies for dedicated tools, such as quality classifiers. |

- Installation check:
```python
import data_juicer as dj
print(dj.__version__)
```

## Quick Start


### Data Processing

- Run `process_data.py` tool with your config as the argument to process
  your dataset.

```shell
python tools/process_data.py --config configs/demo/process.yaml
```

- **Note:** For some operators that involve third-party models or resources which are not stored locally on your computer, it might be slow for the first running because these ops need to download corresponding resources into a directory first.
The default download cache directory is `~/.cache/data_juicer`. Change the cache location by setting the shell environment variable, `DATA_JUICER_CACHE_HOME` to another directory, and you can also change `DATA_JUICER_MODELS_CACHE` or `DATA_JUICER_ASSETS_CACHE` in the same way:

```shell
# cache home
export DATA_JUICER_CACHE_HOME="/path/to/another/directory"
# cache models
export DATA_JUICER_MODELS_CACHE="/path/to/another/directory/models"
# cache assets
export DATA_JUICER_ASSETS_CACHE="/path/to/another/directory/assets"
```

### Data Analysis
- Run `analyze_data.py` tool with your config as the argument to analyse your dataset.

```shell
python tools/analyze_data.py --config configs/demo/analyser.yaml
```

- **Note:** Analyser only compute stats of Filter ops. So extra Mapper or Deduplicator ops will be ignored in the analysis process.

### Data Visualization

- Run `app.py` tool to visualize your dataset in your browser.

```shell
streamlit run app.py
```

### Build Up Config Files

- Config files specify some global arguments, and an operator list for the
  data process. You need to set:
  - Global arguments: input/output dataset path, number of workers, etc.
  - Operator list: list operators with their arguments used to process the dataset.
- You can build up your own config files by:
  - ➖：Modify from our example config file [`config_all.yaml`](configs/config_all.yaml) which includes **all** ops and default
    arguments. You just need to **remove** ops that you won't use and refine
    some arguments of ops.
  - ➕：Build up your own config files **from scratch**. You can refer our
    example config file [`config_all.yaml`](configs/config_all.yaml), [op documents](docs/Operators.md), and advanced [Build-Up Guide for developers](docs/DeveloperGuide.md#build-your-own-configs).
  - Besides the yaml files, you also have the flexibility to specify just
    one (of several) parameters on the command line, which will override
    the values in yaml files.

```shell
python xxx.py --config configs/demo/process.yaml --language_id_score_filter.lang=en
```

- The basic config format and definition is shown below.

  ![Basic config example of format and definition](docs/imgs/config-def-EN.jpg "Basic config file example")

### Preprocess Raw Data (Optional)
- Our formatters support some common input dataset formats for now:
  - Multi-sample in one file: jsonl/json, parquet, csv/tsv, etc.
  - Single-sample in one file: txt, code, docx, pdf, etc.
- However, data from different sources are complicated and diverse. Such as:
  - [Raw arxiv data downloaded from S3](https://info.arxiv.org/help/bulk_data_s3.html) include thousands of tar files and even more gzip files in them, and expected tex files are embedded in the gzip files so they are hard to obtain directly.
  - Some crawled data include different kinds of files (pdf, html, docx, etc.). And extra information like tables, charts, and so on is hard to extract.
- It's impossible to handle all kinds of data in Data-Juicer, issues/PRs are welcome to contribute to process new data types!
- Thus, we provide some **common preprocessing tools** in [`tools/preprocess`](tools/preprocess/) for you to preprocess these data.
  - You are welcome to make your contributions to new preprocessing tools for the community.
  - We **highly recommend** that complicated data can be preprocessed to jsonl or parquet files.

## Documentation | 文档 <a name="documentation"/>

- [Overview](README.md) | [概览](README_ZH.md)
- [Operator Zoo](docs/Operators.md) | [算子库](docs/Operators_ZH.md)
- [Configs](configs/README.md) | [配置系统](configs/README_ZH.md)
- [Developer Guide](docs/DeveloperGuide.md) | [开发者指南](docs/DeveloperGuide_ZH.md)
- Dedicated Toolkits | 专用工具箱
  - [Quality Classifier](tools/quality_classifier/README.md) | [质量分类器](tools/quality_classifier/README_ZH.md)
  - [Auto Evaluation](tools/evaluator/README.md) | [自动评测](tools/evaluator/README_ZH.md)
  - [Preprocess](tools/preprocess/README.md) | [前处理](tools/preprocess/README_ZH.md)
  - [Postprocess](tools/postprocess/README.md) | [后处理](tools/postprocess/README_ZH.md)
- [Third-parties (LLM Ecosystems)](thirdparty/README.md) | [第三方库（大语言模型生态）](thirdparty/README_ZH.md)
- [API references](https://alibaba.github.io/data-juicer/)

## Data Recipes
- [Recipes for data process in BLOOM](configs/bloom/README.md)
- [Recipes for data process in RedPajama](configs/redpajama/README.md)
- [Refined recipes for pretraining data](configs/refine_recipe/README.md)
- [Refined recipes for SFT data](configs/refine_recipe/README.md#L28)

## Demos
- Introduction to Data-Juicer [[ModelScope](https://modelscope.cn/studios/Data-Juicer/overview_scan/summary)]
- Data Visualization:
  - Basic Statistics [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_visulization_statistics/summary)]
  - Lexical Diversity [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_visulization_diversity/summary)]
  - Operator Effect [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_visulization_op_effect/summary)]
- Data Processing:
  - Scientific Literature (e.g. [ArXiv](https://info.arxiv.org/help/bulk_data_s3.html)) [[ModelScope](https://modelscope.cn/studios/Data-Juicer/process_sci_data/summary)]
  - Programming Code (e.g. [TheStack](https://huggingface.co/datasets/bigcode/the-stack)) [[ModelScope](https://modelscope.cn/studios/Data-Juicer/process_code_data/summary)]
  - Chinese Instruction Data (e.g. [Alpaca-CoT](https://huggingface.co/QingyiSi/Alpaca-CoT)) [[ModelScope](https://modelscope.cn/studios/Data-Juicer/sft_data_zh/summary)]
- Tool Pool:
  - Quality Classifier for CommonCrawl [[ModelScope](https://modelscope.cn/studios/Data-Juicer/tool_quality_classifier/summary)]
  - Auto Evaluation on [HELM](https://github.com/stanford-crfm/helm) [[ModelScope](https://modelscope.cn/studios/Data-Juicer/auto_evaluation_helm/summary)]
  - Data Sampling and Mixture [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_mixture/summary)]
- Data Process Loop [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_process_loop/summary)]
- Data Process HPO [[ModelScope](https://modelscope.cn/studios/Data-Juicer/data_process_hpo/summary)]

## License
Data-Juicer is released under Apache License 2.0.

## Contributing
We greatly welcome contributions of new features, bug fixes, and discussions. Please refer to [How-to Guide for Developers](docs/DeveloperGuide.md).

## References
Our paper is coming soon!
