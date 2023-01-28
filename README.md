# nameforme

A helper python package that can be used to generate names based on the [`dateset`](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-03-22/babynames.csv). This could be used to come up with baby names, character names, pseudonyms, etc. 

Source Data: Contains baby names born in the United States for each year from 1880 to 2017, and the number of children of each sex given each name. Names must appear at least 5 times in each year to be included. (Source: http://www.ssa.gov/oact/babynames/limits.html)

This package is similar to the existing [names](https://pypi.org/project/names/) package by Trey Hunner (last updated in 2014), however, our uses a more recent dataset (with names up to 2017), and more options for users to customize what type of names to generate, including the ability to generate similar sounding names.

You can check the online documentation of this package on [readthedocs](https://nameforme.readthedocs.io/en/main/index.html).

## Features
Note that the name of the functions is not finalized. They are subject to change.

The package is an assimilation of four independent functions:

- `find_unisex_name`: Generate a random set of 10 suggested neutral baby names based on the given limitation and baby names in the past years.

- `find_old_name`: Generate a random set of 10 suggested neutral(by default) baby names based on the given time period and sex.

- `find_similar_name`: Generate a random set of 10 suggested similar baby names based on the syllable of the input name. 

- `find_name`: Generate a random set of 10 suggested baby names based on the given limitations.

## Installation

```bash
$ pip install nameforme
```

## Usage

Below is a basic example of how to use each of the four functions included in this package.

```
# Load all required package functions
from nameforme.nameforme import find_name
from nameforme.nameforme import find_old_name
from nameforme.nameforme import find_similar_name
from nameforme.nameforme import find_unisex_name

# Generate a random set of 10 suggested baby names based on the given limitations.
# if the given limitation can match to at least 10 names, a list of 10 names will be provided
find_name("F", "A", length=3)
#if the given limitation can only match less than 10 names, all matched names will be provided
find_name("m", "b", length=9)

# Generate a random set of suggested neutral(by default) baby names based on the given time period and sex.
find_old_name('1980s', limit=3)

# Generate a random list of names that sound similar to a given user input name.
find_similar_name('Daniel', limit=20)

# Generate the a random set of suggested neutral baby names based on the given limitation and baby names in the past years.
find_unisex_name(bar=0.02,limit=10)
```

## Dependencies
- python = "3.9"
- numpy = "1.24.1"
- pandas = "1.5.3"
- jellyfish = "0.9.0"
- pytest = "7.2.1"
- sphinx = "6.1.3"

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`nameforme` was created by Daniel Cairns, Eyre Hong, Bruce Wu, Zilong Yi (UBC MDS). It is licensed under the terms of the MIT license.

## Credits

`nameforme` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
