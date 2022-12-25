# 🎄 Advent of Code 🎄

![AoC2022 logo](https://blog.pythondiscord.com/content/images/2021/03/AoC_banner.png)

## About

Advent of Code is an annual Advent calendar of programming puzzles.

## Summary

A template maker project for [Advent of Code](https://adventofcode.com) written in python along with solutions to puzzles.
The core aim of this project is to automate extraction of puzzle problem, input data and submission of answers. 
You just need to focus on writing logical code to solve the part 1 and part 2 of puzzle problem.

## Usage

The project use [poetry](https://python-poetry.org) for project manager.
Clone this repository and run `poetry install` to install dependencies:

    $ git clone https://github.com/coff33Overflow/advent-of-code aoc-python
    $ cd advent-of-code

    # install dependencies
    $ poetry install

    # run the day01
    # poetry run python -m aoc.2022.day01

## Generate

You can generate all necessary files for use in the event with a simple
command:

    $ poetry run python -m aoc.gen -y2022 -d01

This command generate these files:

    * creating /aoc/day01/input.txt
    * creating /aoc/day01/__main__.py
    * creating /aoc/day01/part1.py
    * creating /aoc/day01/part2.py

- `/aoc/day01/input.txt`: you can insert here the input data.
- `/aoc/day01/problem.txt`: you can find the puzzle problem statement here .
- `/aoc/day01/__main__.py`: is the main module.
- `/aoc/day01/part1.py`: solution for part 1.
- `/aoc/day01/part2.py`: solution for part 2.

## Declare your dependencies

Pin dependencies in `poetry.lock`. 
Adding **beautifulsoup4 = "4.10.0"**, you’re telling Poetry that it should install exactly this version. 
When you add a requirement to the `pyproject.toml` file, it’s not installed yet.

    rp_poetry/pyproject.toml (Excerpt)

    [tool.poetry.dependencies]
    python = "^3.9"
    requests = "^2.26.0"
    beautifulsoup4 = "4.10.0"


By running poetry lock, Poetry processes all dependencies in your pyproject.toml file 
and locks them into the `poetry.lock` file

    $ poetry lock

Install dependencies with `poetry.lock`

    $ poetry install

To learn more about poetry, read this documentation: https://realpython.com/dependency-management-python-poetry/

> Note:
> You can avoid the generation of the folder `__pycache__` set this environment
> variable `export PYTHONDONTWRITEBYTECODE=1` or pass the `-B` flag
> after python command.

Folder structure:

    ├── aoc
    │    ├── year
    │    │     └── day
    │    │          ├── __main__.py
    │    │          │── part1.py
    │    │          │── part2.py
    │    │          │── problem.txt
    │    │          └── input.txt 
    │    └── utils
    │          └── aoc_utils.py 

Happy coding!
<br>

## Author
**Devashish Somani**
<br>
[Github](https://github.com/coff33Overflow) 
<br>
[Email](mailto:devashishsomani1995@gmail.com)

<br>
<br>
<p align="center">
<img src="https://wp.technologyreview.com/wp-content/uploads/2021/12/aoc-santa-hat.gif" width="250" height="250"/>
<img src="https://eduherminio.github.io/assets/images/2020-11-26-getting-ready-for-aoc-2020/aoc_2015.gif" width="250" height="250"/>
<img src="https://wp.technologyreview.com/wp-content/uploads/2021/12/reindeer.gif" width="250" height="250"/>
</p>

