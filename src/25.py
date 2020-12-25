#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    card_pub, door_pub = tuple(map(int, inputTxt.splitlines()))

    card_loop = 0
    while pow(7, card_loop, 20201227) != card_pub:
        card_loop += 1

    return pow(door_pub, card_loop, 20201227)


def b(inputTxt: str) -> str:
    return "Merry Christmas!"


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
