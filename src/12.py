#!/usr/bin/env python3

import sys
from math import cos, sin, pi, sqrt, tan, atan2


def a(inputTxt: str) -> int:
    directions = []
    for line in inputTxt.splitlines():
        directions.append((line[0], int(line[1:])))

    x, y = (0, 0)
    angle = 0
    for d, n in directions:
        if d == "N":
            y += n
        elif d == "S":
            y -= n
        elif d == "E":
            x += n
        elif d == "W":
            x -= n
        elif d == "L":
            angle += n * pi / 180
        elif d == "R":
            angle -= n * pi / 180
        elif d == "F":
            x += n * cos(angle)
            y += n * sin(angle)
    return round(abs(x) + abs(y))


def b(inputTxt: str) -> int:
    directions = []
    for line in inputTxt.splitlines():
        directions.append((line[0], int(line[1:])))

    x, y = (0, 0)
    wx, wy = (10, 1)
    for d, n in directions:
        if d == "N":
            wy += n
        elif d == "S":
            wy -= n
        elif d == "E":
            wx += n
        elif d == "W":
            wx -= n
        elif d == "L":
            m = sqrt(wy ** 2 + wx ** 2)
            o = atan2(wy, wx)
            wx = m * cos(o + n * pi / 180)
            wy = m * sin(o + n * pi / 180)
        elif d == "R":
            m = sqrt(wy ** 2 + wx ** 2)
            o = atan2(wy, wx)
            wx = m * cos(o - n * pi / 180)
            wy = m * sin(o - n * pi / 180)
        elif d == "F":
            x += n * wx
            y += n * wy
    return round(abs(x) + abs(y))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
