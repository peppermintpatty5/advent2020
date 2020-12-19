#!/usr/bin/env python3

import sys


def halfIt(lo: int, hi: int, steps: str, sig: str) -> int:
    for c in steps:
        if c == sig:
            hi = (hi + lo) // 2
        else:
            lo = (hi + lo) // 2 + 1
    return lo


def a(inputTxt: str) -> int:
    seatIDs = set()
    for line in inputTxt.splitlines():
        row = halfIt(0, 127, line[:7], "F")
        col = halfIt(0, 7, line[7:], "L")
        seatIDs.add(row * 8 + col)
    return max(seatIDs)


def b(inputTxt: str) -> int:
    seatIDs = set(range(128, 947))
    for line in inputTxt.splitlines():
        row = halfIt(0, 127, line[:7], "F")
        col = halfIt(0, 7, line[7:], "L")
        seatIDs.discard(row * 8 + col)
    return seatIDs.pop()


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
