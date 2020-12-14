#!/usr/bin/env python3

from math import ceil


def a():
    with open("input.txt") as f:
        e = int(next(f))
        schedule = [int(x) for x in next(f).strip().split(",") if x != "x"]

    f = lambda t: t - (e % t)
    m = min(schedule, key=lambda t: f(t))
    return m * f(m)


def b():
    with open("input.txt") as f:
        next(f)
        s = [int(x) if x != "x" else 1 for x in next(f).strip().split(",")]

    # for i in range(len(s)):
    #     if s[i] != 1:
    #         print(f"{-i}, {s[i]}")


print(a(), b(), sep="\n")
