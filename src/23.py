#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    cups = list(map(int, "123487596"))
    n = len(cups)
    current = cups[0]

    for i in range(100):
        pickUp = []
        for j in range(3):
            pickUp.append(
                cups.pop((cups.index(current) + 1) % len(cups)),
            )

        for j in range(1, n):
            dest = (current - j) % (n + 1)
            if dest in cups:
                break

        for j in range(3):
            cups.insert(
                cups.index(dest) + j + 1,
                pickUp.pop(0),
            )

        current = cups[(cups.index(current) + 1) % n]

    order = []
    for i in range(n - 1):
        order.append(cups[(cups.index(1) + i + 1) % n])
    return "".join(str(i) for i in order)


def b(inputTxt: str) -> int:
    left = {}
    right = {}
    firstFewCups = list(map(int, inputTxt.strip()))

    prev = None
    for cup in firstFewCups:
        left[cup] = prev
        right[prev] = cup
        prev = cup
    for cup in range(10, 1000001):
        left[cup] = prev
        right[prev] = cup
        prev = cup
    left[firstFewCups[0]] = prev
    right[prev] = firstFewCups[0]
    right.pop(None)

    n = len(left)
    current = firstFewCups[0]
    for i in range(10000000):
        pickUp = []
        x = current
        for j in range(3):
            x = right[x]
            pickUp.append(x)
        for j in range(1, n):
            dest = (current - j) % (n + 1)
            if dest != 0 and dest not in pickUp:
                break
        """
        INITIAL STATE
            current <=> pickUp[0] <=> pickUp[1] <=> pickUp[2] <=> right[pickUp[2]]
            AND
            dest <=> right[dest]
        FINAL STATE
            current <=> right[pickUp[2]]
            AND
            dest <=> pickUp[0] <=> pickUp[1] <=> pickUp[2] <=> right[dest]
        """
        right[current] = right[pickUp[2]]
        left[right[pickUp[2]]] = current

        right[pickUp[2]] = right[dest]
        left[right[dest]] = pickUp[2]

        right[dest] = pickUp[0]
        left[pickUp[0]] = dest

        current = right[current]

    return right[1] * right[right[1]]


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
