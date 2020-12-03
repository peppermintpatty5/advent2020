#!/usr/bin/env python3


def a():
    count = 0
    x = 0
    with open("input.txt") as f:
        for line in f:
            if line[x % len(line.strip())] == "#":
                count += 1
            x += 3
    return count


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


def b():
    with open("input.txt") as f:
        grid = [line.strip() for line in f]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    prod = 1
    for right, down in slopes:
        prod *= sled(right, down, grid)
    return prod


print(a(), b(), sep="\n")
