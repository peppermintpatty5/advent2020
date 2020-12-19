#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    count = 0
    responses = []
    for line in inputTxt.splitlines():
        if line == "":
            count += len(set.union(*responses))
            responses.clear()
        else:
            responses.append(set(line))
    return count + len(set.union(*responses))


def b(inputTxt: str) -> int:
    count = 0
    responses = []
    for line in inputTxt.splitlines():
        if line == "":
            count += len(set.intersection(*responses))
            responses.clear()
        else:
            responses.append(set(line))
    return count + len(set.intersection(*responses))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
