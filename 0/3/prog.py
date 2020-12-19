#!/usr/bin/env python3

import sys


def sled(right: int, down: int, grid: list) -> int:
    count = 0
    x, y = (0, 0)
    while y < len(grid):
        line = grid[y]
        if line[x % len(line)] == "#":
            count += 1
        x += right
        y += down
    return count


def a(inputTxt: str) -> int:
    grid = inputTxt.splitlines()
    return sled(3, 1, grid)


def b(inputTxt: str) -> int:
    grid = inputTxt.splitlines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for right, down in slopes:
        prod *= sled(right, down, grid)
    return prod


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
