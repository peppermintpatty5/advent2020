#!/usr/bin/env python3

import sys
from math import ceil


def a(inputTxt: str) -> int:
    lines = inputTxt.splitlines()
    e = int(lines[0])
    schedule = [int(x) for x in lines[1].split(",") if x != "x"]

    f = lambda t: t - (e % t)
    m = min(schedule, key=lambda t: f(t))
    return m * f(m)


def b(inputTxt: str) -> int:
    ...


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
