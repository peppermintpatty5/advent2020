#!/usr/bin/env python3


def halfIt(lo: int, hi: int, steps: str, sig: str) -> int:
    for c in steps:
        if c == sig:
            hi = (hi + lo) // 2
        else:
            lo = (hi + lo) // 2 + 1
    return lo


def a():
    seatIDs = set()
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            row = halfIt(0, 127, line[:7], "F")
            col = halfIt(0, 7, line[7:], "L")
            seatIDs.add(row * 8 + col)
    return max(seatIDs)


def b():
    seatIDs = set(range(128, 947))
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            row = halfIt(0, 127, line[:7], "F")
            col = halfIt(0, 7, line[7:], "L")
            seatIDs.discard(row * 8 + col)
    return seatIDs.pop()


print(a(), b(), sep="\n")
