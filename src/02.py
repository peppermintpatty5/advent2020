#!/usr/bin/env python3

import re
import sys


def a(inputTxt: str) -> int:
    count = 0
    for line in inputTxt.splitlines():
        a, b, letter, passwd = re.split(r"[-: ]+", line)
        if int(a) <= passwd.count(letter) <= int(b):
            count += 1
    return count


def b(inputTxt: str) -> int:
    count = 0
    for line in inputTxt.splitlines():
        a, b, letter, passwd = re.split(r"[-: ]+", line)
        if (passwd[int(a) - 1] == letter) != (passwd[int(b) - 1] == letter):
            count += 1
    return count


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
