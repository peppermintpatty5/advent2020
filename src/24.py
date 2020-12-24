#!/usr/bin/env python3

import sys


def splitDirections(line: str) -> list:
    directions = []
    i = 0
    while i < len(line):
        if line[i] == "n" or line[i] == "s":
            directions.append(line[i : i + 2])
            i += 2
        else:
            directions.append(line[i])
            i += 1
    return directions


def move(x: int, y: int, direction: str) -> tuple:
    stagger = y % 2  # honeycomb staggering

    if direction == "e":
        return (x + 1, y)
    elif direction == "w":
        return (x - 1, y)
    elif direction == "nw":
        return (x - 1 + stagger, y + 1)
    elif direction == "sw":
        return (x - 1 + stagger, y - 1)
    elif direction == "ne":
        return (x + stagger, y + 1)
    elif direction == "se":
        return (x + stagger, y - 1)


def a(inputTxt: str) -> int:
    black = set()
    for line in inputTxt.splitlines():
        x, y = (0, 0)
        for direction in splitDirections(line):
            x, y = move(x, y, direction)
        black ^= {(x, y)}
    return len(black)


def adj(x: int, y: int) -> set:
    stagger = y % 2

    return {
        (x + 1, y),
        (x - 1, y),
        (x - 1 + stagger, y + 1),
        (x - 1 + stagger, y - 1),
        (x + stagger, y + 1),
        (x + stagger, y - 1),
    }


def b(inputTxt: str) -> int:
    black = set()
    for line in inputTxt.splitlines():
        x, y = (0, 0)
        for direction in splitDirections(line):
            x, y = move(x, y, direction)
        black ^= {(x, y)}

    for _ in range(100):
        nextBlack = set()
        for tile in set.union(*(adj(x, y) for x, y in black)):
            if tile in black:
                if len(adj(*tile) & black) in {1, 2}:
                    nextBlack.add(tile)
            else:
                if len(adj(*tile) & black) == 2:
                    nextBlack.add(tile)
        black = nextBlack
    return len(black)


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
