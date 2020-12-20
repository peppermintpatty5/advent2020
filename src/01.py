#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    nums = {int(line) for line in inputTxt.splitlines()}

    for x in nums:
        y = 2020 - x
        if y in nums:
            return x * y


def b(inputTxt: str) -> int:
    nums = {int(line) for line in inputTxt.splitlines()}

    for x in nums:
        for y in nums:
            z = 2020 - x - y
            if z in nums:
                return x * y * z


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
