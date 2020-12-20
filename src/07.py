#!/usr/bin/env python3

import sys


def a(inputTxt: str) -> int:
    bags = {}
    for line in inputTxt.splitlines():
        if line.endswith("no other bags."):
            continue

        a, b = line.split(" bags contain ")
        outer = a
        inner = [" ".join(x.split(" ")[1:3]) for x in b.split(", ")]
        bags[outer] = inner

    gold = set()  # all bags that reduce to shiny gold
    while True:
        newGold = set()
        for outer, inner in bags.items():
            if any(bag == "shiny gold" or bag in gold for bag in inner):
                newGold.add(outer)

        if len(newGold - gold) > 0:
            gold |= newGold
        else:
            break

    return len(gold)


def countReduce(bag: str, bags: dict, quantities: dict) -> int:
    if bag in bags:
        return sum(
            q + q * countReduce(inner, bags, quantities)
            for q, inner in zip(quantities[bag], bags[bag])
        )
    else:
        return 0


def b(inputTxt: str) -> int:
    bags = {}
    quantities = {}
    for line in inputTxt.splitlines():
        if line.endswith("no other bags."):
            continue

        a, b = line.split(" bags contain ")
        outer = a
        inner = [" ".join(x.split(" ")[1:3]) for x in b.split(", ")]
        q = [int(x.split(" ")[0]) for x in b.split(", ")]
        bags[outer] = inner
        quantities[outer] = q

    return countReduce("shiny gold", bags, quantities)


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
