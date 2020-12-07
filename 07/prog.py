#!/usr/bin/env python3


def a():
    bags = {}
    with open("input.txt") as f:
        for line in f:
            line = line.strip()[:-1]  # truncate period + newline
            if line.endswith("no other bags"):
                continue

            a, b = line.split(" bags contain ")
            outer = a
            inner = [" ".join(x.split(" ")[1:3]) for x in b.split(", ")]
            bags[outer] = inner

    gold = {"shiny gold"}  # all bags that reduce to shiny gold
    for i in range(10):  # try out different values until stable lol
        for outer, inner in bags.items():
            for bag in inner:
                if bag in gold:
                    gold.add(outer)
                    break
    return len(gold) - 1


def countReduce(bag: str, bags: dict, quantities: dict) -> int:
    if bag not in bags:
        return 0
    else:
        return sum(
            q + q * countReduce(inner, bags, quantities)
            for q, inner in zip(quantities[bag], bags[bag])
        )


def b():
    bags = {}
    quantities = {}
    with open("input.txt") as f:
        for line in f:
            line = line.strip()[:-1]
            if line.endswith("no other bags"):
                continue

            a, b = line.split(" bags contain ")
            outer = a
            inner = [" ".join(x.split(" ")[1:3]) for x in b.split(", ")]
            q = [int(x.split(" ")[0]) for x in b.split(", ")]
            bags[outer] = inner
            quantities[outer] = q
    return countReduce("shiny gold", bags, quantities)


print(a(), b(), sep="\n")
