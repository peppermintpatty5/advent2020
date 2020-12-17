#!/usr/bin/env python3

from itertools import product


def adj(*t: int) -> set:
    return set(product(*({u - 1, u, u + 1} for u in t))) - {tuple(t)}


def a():
    with open("input.txt") as f:
        start = f.read().strip()

    active = set()
    for y, row in enumerate(start.split("\n")):
        for x, cell in enumerate(row):
            if cell == "#":
                active.add((x, y, 0))

    for cycle in range(6):
        nextActive = set()
        for coord in set.union(*(adj(*t) for t in active)):
            if coord in active:
                if len(adj(*coord) & active) in {2, 3}:
                    nextActive.add(coord)
            else:
                if len(adj(*coord) & active) == 3:
                    nextActive.add(coord)
        active = nextActive

    return len(active)


def b():
    with open("input.txt") as f:
        start = f.read().strip()

    active = set()
    for y, row in enumerate(start.split("\n")):
        for x, cell in enumerate(row):
            if cell == "#":
                active.add((x, y, 0, 0))

    for cycle in range(6):
        nextActive = set()
        for coord in set.union(*(adj(*t) for t in active)):
            if coord in active:
                if len(adj(*coord) & active) in {2, 3}:
                    nextActive.add(coord)
            else:
                if len(adj(*coord) & active) == 3:
                    nextActive.add(coord)
        active = nextActive

    return len(active)


print(a(), b(), sep="\n")
