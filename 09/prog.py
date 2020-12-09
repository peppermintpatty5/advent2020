#!/usr/bin/env python3


def pairSum(num: int, l: list) -> tuple:
    s = set(l)
    for x in s:
        y = num - x
        if y in s and x != y:
            return (x, y)
    return None


def a():
    with open("input.txt") as f:
        nums = list(map(int, f))

    for i in range(25, len(nums)):
        num = nums[i]
        if pairSum(num, nums[i - 25 : i]) is None:
            return num


def b():
    goal = a()
    with open("input.txt") as f:
        nums = list(map(int, f))

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            x = sum(nums[i:j])
            if x == goal:
                return min(nums[i:j]) + max(nums[i:j])
            elif x > goal:
                break


print(a(), b(), sep="\n")
