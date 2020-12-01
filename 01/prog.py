#!/usr/bin/env python3


def a():
    nums = set()
    with open("input.txt") as f:
        for line in f:
            nums.add(int(line))

    for x in nums:
        y = 2020 - x
        if y in nums:
            return x * y


def b():
    nums = set()
    with open("input.txt") as f:
        for line in f:
            nums.add(int(line))

    for x in nums:
        for y in nums:
            z = 2020 - x - y
            if z in nums:
                return x * y * z


print(a(), b(), sep="\n")
