![GitHub pull requests](https://img.shields.io/github/issues-pr/Silly-Machine/TuPi-Portuguese-Hate-Speech-Dataset)
[![GitHub issues](https://img.shields.io/github/issues/Silly-Machine/TuPi-Portuguese-Hate-Speech-Dataset.svg)](https://img.shields.io/github/issues/Silly-Machine/TuPi-Portuguese-Hate-Speech-Dataset.svg)
![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Silly-Machine/TuPi-Portuguese-Hate-Speech-Dataset/main)
[![GitHub license](https://img.shields.io/badge/license-MIT-orange)](https://opensource.org/license/mit/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-orange.svg)](https://www.python.org/downloads/release/python-3100/)

# Portuguese Hate Speech Dataset (TuPI)

This repository contains the processes used to create the Portuguese hate speech dataset (TuPy), an annotated corpus designed to facilitate the development of advanced hate speech detection models using machine learning (ML) and natural language processing (NLP) techniques. TuPI is formed by combining datasets annotated by [Fortuna *et. al.*](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset) (2019), [Leite *et. al.*](https://github.com/JAugusto97/ToLD-Br) (2021), [Vargas *et. al.*](https://github.com/franciellevargas/HateBR) (2020) in addition to 10 thousand unpublished annotated documents collected in 2023.

This repository is organized as follows:

```sh
root.
    ├── datasets 
    ├── figures
    ├── notebooks
    ├── models
    ├── notebooks
    ├── src
    ├── LICENSE
    └── README.md
```

## Quick start

Run the following command

```sh
bash INIT.sh
```

Or install Miniconda 3 than type the following command order:

```sh
conda create -n tupi-env python=3.10
conda activate tupi-env
pip install poetry
poetry install
poetry run python -m nltk.downloader stopwords
```

## Acknowledge
The TuPi project is the result of the development of Felipe Oliveira's thesis and the work of several collaborators. This project is financed by the Federal University of Rio de Janeiro ([UFRJ](https://ufrj.br/)) and the Alberto Luiz Coimbra Institute for Postgraduate Studies and Research in Engineering ([COPPE](https://coppe.ufrj.br/)).
