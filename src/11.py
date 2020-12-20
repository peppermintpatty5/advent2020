#!/usr/bin/env python3

import sys
from itertools import product


ADJ_OFFSETS = set(product({-1, 0, 1}, repeat=2)) - {(0, 0)}


def countAdj(grid: list, r0: int, c0: int) -> int:
    count = 0
    for (dr, dc) in ADJ_OFFSETS:
        r, c = r0 + dr, c0 + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "#":
            count += 1
    return count


def stepA(grid: list) -> list:
    rows = len(grid)
    cols = len(grid[0])
    newGrid = []

    for r in range(rows):
        newRow = []
        for c in range(cols):
            cell = grid[r][c]
            if cell == "L" and countAdj(grid, r, c) == 0:
                newRow.append("#")
            elif cell == "#" and countAdj(grid, r, c) >= 4:
                newRow.append("L")
            else:
                newRow.append(cell)
        newGrid.append(newRow)
    return newGrid


def a(inputTxt: str) -> int:
    grid = inputTxt.splitlines()

    while True:
        newGrid = stepA(grid)
        if grid == newGrid:
            return sum(row.count("#") for row in grid)
        else:
            grid = newGrid


def countFar(grid: list, r0: int, c0: int) -> int:
    count = 0
    for (dr, dc) in ADJ_OFFSETS:
        r, c = r0 + dr, c0 + dc
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            if grid[r][c] in "#L":
                if grid[r][c] == "#":
                    count += 1
                break
            else:
                r += dr
                c += dc
    return count


def stepB(grid: list) -> list:
    rows = len(grid)
    cols = len(grid[0])
    newGrid = []

    for r in range(rows):
        newRow = []
        for c in range(cols):
            cell = grid[r][c]
            if cell == "L" and countFar(grid, r, c) == 0:
                newRow.append("#")
            elif cell == "#" and countFar(grid, r, c) >= 5:
                newRow.append("L")
            else:
                newRow.append(cell)
        newGrid.append("".join(newRow))
    return newGrid


def b(inputTxt: str) -> int:
    grid = inputTxt.splitlines()

    while True:
        newGrid = stepB(grid)
        if grid == newGrid:
            return sum(row.count("#") for row in grid)
        else:
            grid = newGrid


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
