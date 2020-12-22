#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    L = []
    I = set()
    A = set()
    R = []
    for line in inputTxt.splitlines():
        a, b = line[:-1].split(" (contains ")
        ingredients = set(a.split(" "))
        allergens = set(b.split(", "))
        A |= allergens
        I |= ingredients
        L.append(ingredients)
        R.append(allergens)

    f = {}
    for a in A:
        x = set.intersection(*(l for l, r in zip(L, R) if a in r))
        f[a] = x
    possibleAllergens = set.union(*f.values())
    count = 0
    for i in I:
        if i not in possibleAllergens:
            count += sum(1 for l in L if i in l)
    return count


def b(inputTxt: str) -> str:
    L = []
    I = set()
    A = set()
    R = []
    for line in inputTxt.splitlines():
        a, b = line[:-1].split(" (contains ")
        ingredients = set(a.split(" "))
        allergens = set(b.split(", "))
        A |= allergens
        I |= ingredients
        L.append(ingredients)
        R.append(allergens)

    f = {}
    for a in A:
        x = set.intersection(*(l for l, r in zip(L, R) if a in r))
        f[a] = x

    g = {}
    while len(f) > 0:
        for a, x in f.items():
            if len(x) == 1:
                break
        i = x.pop()
        f.pop(a)
        g[i] = a
        for a, x in f.items():
            x.discard(i)
    return ",".join(sorted(g, key=g.get))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
