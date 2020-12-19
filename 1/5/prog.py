#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    start = list(map(int, inputTxt.split(",")))

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


def b(inputTxt: str) -> int:
    start = list(map(int, inputTxt.split(",")))

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


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
