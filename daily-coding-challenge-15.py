"""
Problem:
Given a stream of elements too large to store in memory, pick a random element from the
stream with uniform probability.
"""

from random import randint
import matplotlib.pyplot as plt
from typing import Generator


def element_stream() -> Generator[int, None, None]:
    while True:
        yield randint(1, 10_000)


def random_selector(generator: Generator[int, None, None]) -> int:
    arr = [next(generator) for i in range(10)]
    pos = randint(0, 9)
    return arr[pos]


if __name__ == "__main__":
    generator = element_stream()
    values = []
    for i in range(100_000):
        values.append(random_selector(generator))
    plt.hist(values, edgecolor="black")
    plt.show()
