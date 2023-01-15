# nameforme

A package used to generate names based on the [`dateset`](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv).

Data: for each year from 1880 to 2017, the number of children of each sex given each name. All names with more than 5 uses are given. (Source: http://www.ssa.gov/oact/babynames/limits.html)

Note that the functionality of this package does not overlap with other packages. However, this package only works for generating English names. 

## Installation

```bash
$ pip install nameforme
```

## Usage

- This section will be updated later.


## Feature
Note that the name of functions are not finalized. They are subject to change.
a
The package is an assimilation of four independent functions:

- `find_unisex_name`: Generate the a random set of 10 suggested neutral baby names based on the given limitation and baby names in the past years.

- `find_old_name`: Generate the a random set of 10 suggested neutral(by default) baby names based on the given time period and sex.

- `find_similar_name`: Generate the a random set of 10 suggested similar baby names based on the syllable of the input name. 

- `find_name`: Generate the a random set of 10 suggested baby names based on the given limitations.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`nameforme` was created by Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS). It is licensed under the terms of the MIT license.

## Credits

`nameforme` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
