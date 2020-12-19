#!/usr/bin/env python3

import re
import sys


def partition(l: list, sep, limit=-1) -> list:
    i = -1
    subLists = []

    while limit < 0 or len(subLists) < limit:
        try:
            j = l.index(sep, i + 1)
        except ValueError as e:
            break

        subLists.append(l[i + 1 : j])
        i = j

    subLists.append(l[i + 1 :])
    return subLists


def a(inputTxt: str) -> int:
    count = 0
    validation = []

    notesPg, yourTickPg, nearbyTickPg = partition(inputTxt.splitlines(), "")

    for line in notesPg:
        label, a, b, c, d = re.split(r": |-| or ", line)
        validation.append(range(int(a), int(b) + 1))
        validation.append(range(int(c), int(d) + 1))

    for line in nearbyTickPg[1:]:
        for val in map(int, line.split(",")):
            if not any(val in r for r in validation):
                count += val
                break
    return count


def b(inputTxt: str) -> int:
    validation = {}

    notesPg, yourTickPg, nearbyTickPg = partition(inputTxt.splitlines(), "")

    for line in notesPg:
        label, a, b, c, d = re.split(r": |-| or ", line)
        r1 = range(int(a), int(b) + 1)
        r2 = range(int(c), int(d) + 1)
        validation[label] = set(r1) | set(r2)

    myTicket = list(map(int, yourTickPg[1].split(",")))
    n = len(myTicket)

    possibleLabels = {i: set(validation.keys()) for i in range(n)}
    for line in nearbyTickPg[1:]:
        ticket = list(map(int, line.split(",")))
        if not all(any(t in v for v in validation.values()) for t in ticket):
            continue

        for i, t in enumerate(ticket):
            for label, v in validation.items():
                if t not in v:
                    possibleLabels[i].remove(label)

    certainLabels = {}
    while len(possibleLabels) > 0:
        for pos, labels in possibleLabels.items():
            if len(labels) == 1:
                uniqueLabel = labels.pop()
                possibleLabels.pop(pos)
                certainLabels[pos] = uniqueLabel
                break

        for index, labels in possibleLabels.items():
            if pos != index:
                labels.discard(uniqueLabel)

    product = 1
    for pos, label in certainLabels.items():
        if label.startswith("departure"):
            product *= myTicket[pos]

    return product


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
