#!/usr/bin/env python3


def a():
    with open("input.txt") as f:
        start = list(map(int, next(f).split(",")))

    prev = -1
    cache = {}
    for turn in range(2020):
        if turn < len(start):
            num = start[turn]
        elif prev not in cache:
            num = 0
        else:
            num = turn - cache[prev] - 1

        cache[prev] = turn - 1
        prev = num
    return num


def b():
    with open("input.txt") as f:
        start = list(map(int, next(f).split(",")))

    prev = -1
    cache = {}
    for turn in range(30000000):
        if turn < len(start):
            num = start[turn]
        elif prev not in cache:
            num = 0
        else:
            num = turn - cache[prev] - 1

        cache[prev] = turn - 1
        prev = num
    return num


print(a(), b(), sep="\n")
