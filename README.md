# Portuguese Hate Speech Dataset (TuPI)


The Portuguese Hate Speech Dataset (TuPI) is a project that aims to develop models for identifying hate speech. It is formed by combining datasets annotated by [Fortuna *et. al.*](https://github.com/paulafortuna/Portuguese-Hate-Speech-Dataset) (2019), [Leite *et. al.*](https://github.com/JAugusto97/ToLD-Br) (2021), [Vargas *et. al.*](https://github.com/franciellevargas/HateBR) (2020) in addition to 10 thousand unpublished annotated documents collected in 2023.

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
```


## Acknowledge
The TuPi project is the result of the development of Felipe Oliveira's thesis and the work of several caloabores (annotators and developers) with support from the Federal University of Rio de Janeiro ([UFRJ](https://ufrj.br/)) and the Alberto Luiz Coimbra Institute for Postgraduate Studies and Research in Engineering ([COPPE](https://coppe.ufrj.br/)).