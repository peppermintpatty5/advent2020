#!/usr/bin/env python3


def countAdj(grid: list, r0: int, c0: int) -> int:
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            r, c = r0 + dr, c0 + dc
            if (
                (dr != 0 or dc != 0)
                and 0 <= r < len(grid)
                and 0 <= c < len(grid[0])
                and grid[r][c] == "#"
            ):
                count += 1
    return count


def stepA(grid: list) -> list:
    rows = len(grid)
    cols = len(grid[0])
    newGrid = []

    adjGrid = []
    for r in range(rows):
        adjRow = []
        for c in range(cols):
            adjRow.append(countAdj(grid, r, c))
        adjGrid.append(adjRow)

    for r in range(rows):
        newRow = []
        for c in range(cols):
            cell = grid[r][c]
            if cell == "L" and adjGrid[r][c] == 0:
                newRow.append("#")
            elif cell == "#" and adjGrid[r][c] >= 4:
                newRow.append("L")
            else:
                newRow.append(cell)
        newGrid.append(newRow)
    return newGrid


def a():
    with open("input.txt") as f:
        grid = [line.strip() for line in f]

    while True:
        newGrid = stepA(grid)
        if grid == newGrid:
            return sum(row.count("#") for row in grid)
        else:
            grid = newGrid


def countFar(grid: list, r0: int, c0: int) -> int:
    count = 0
    origin = grid[r0][c0]
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr != 0 or dc != 0:
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

    adjGrid = []
    for r in range(rows):
        adjRow = []
        for c in range(cols):
            adjRow.append(countFar(grid, r, c))
        adjGrid.append(adjRow)

    newGrid = []
    for r in range(rows):
        newRow = []
        for c in range(cols):
            cell = grid[r][c]
            if cell == "L" and adjGrid[r][c] == 0:
                newRow.append("#")
            elif cell == "#" and adjGrid[r][c] >= 5:
                newRow.append("L")
            else:
                newRow.append(cell)
        newGrid.append("".join(newRow))
    return newGrid


def b():
    with open("input.txt") as f:
        grid = [line.strip() for line in f]

    while True:
        newGrid = stepB(grid)
        if grid == newGrid:
            return sum(row.count("#") for row in grid)
        else:
            grid = newGrid


print(a(), b(), sep="\n")
