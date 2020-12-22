#!/usr/bin/env python3

import sys


def getLIAR(inputTxt: str):
    A = set()
    I = set()
    L = []
    R = []

    for line in inputTxt.splitlines():
        a, b = line[:-1].split(" (contains ")
        ingredients = set(a.split(" "))
        allergens = set(b.split(", "))
        A.update(allergens)
        I.update(ingredients)
        L.append(ingredients)
        R.append(allergens)

    return L, I, A, R


def a(inputTxt: str) -> int:
    L, I, A, R = getLIAR(inputTxt)
    fin = {a: set.intersection(*(l for l, r in zip(L, R) if a in r)) for a in A}
    impossibleAllergens = I - set.union(*fin.values())

    return sum(sum(1 for l in L if i in l) for i in impossibleAllergens)


def b(inputTxt: str) -> str:
    L, I, A, R = getLIAR(inputTxt)
    fin = {a: set.intersection(*(l for l, r in zip(L, R) if a in r)) for a in A}

    f = {}  # inverse of f function, maps ingredients to allergens
    while len(fin) > 0:
        a, x = next((a, x) for a, x in fin.items() if len(x) == 1)
        i = x.pop()
        fin.pop(a)
        f[i] = a

        for x in fin.values():
            x.discard(i)

    return ",".join(sorted(f, key=f.get))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
