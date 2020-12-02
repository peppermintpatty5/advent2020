#!/usr/bin/env python3


def a():
    count = 0
    with open("input.txt") as f:
        for line in f:
            n, c, pw = line.split(" ")
            c = c[0]
            a, b = [int(x) for x in n.split("-", maxsplit=1)]
            if a <= pw.count(c) <= b:
                count += 1
    return count


def b():
    count = 0
    with open("input.txt") as f:
        for line in f:
            n, c, pw = line.split(" ")
            c = c[0]
            a, b = [int(x) for x in n.split("-", maxsplit=1)]
            if (pw[a - 1] == c) != (pw[b - 1] == c):
                count += 1
    return count


print(a(), b(), sep="\n")
