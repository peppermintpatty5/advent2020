#!/usr/bin/env python3

import sys


def findPairSum(num: int, l: list) -> tuple:
    s = set(l)
    for x in s:
        y = num - x
        if y in s and x != y:
            return (x, y)
    return None


def a(inputTxt: str) -> int:
    nums = list(map(int, inputTxt.splitlines()))

    for i in range(25, len(nums)):
        if findPairSum(nums[i], nums[i - 25 : i]) is None:
            return nums[i]


def b(inputTxt: str) -> int:
    nums = list(map(int, inputTxt.splitlines()))
    goal = a(inputTxt)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x = nums[i:j]
            if sum(x) == goal:
                return min(x) + max(x)
            elif sum(x) > goal:
                break


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
