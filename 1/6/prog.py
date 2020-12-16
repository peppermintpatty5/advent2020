#!/usr/bin/env python3


def a():
    count = 0
    validation = []

    with open("input.txt") as f:
        notesPg, yourTickPg, nearbyTickPg = f.read().strip().split("\n\n")

    for line in notesPg.split("\n"):
        a, b = line.split(": ")
        b1, b2 = b.split(" or ")
        r1 = range(int(b1.split("-")[0]), int(b1.split("-")[1]) + 1)
        r2 = range(int(b2.split("-")[0]), int(b2.split("-")[1]) + 1)
        validation.append(r1)
        validation.append(r2)

    for line in nearbyTickPg.split("\n")[1:]:
        for val in map(int, line.split(",")):
            if not any(val in r for r in validation):
                count += val
                break
    return count


def b():
    validation = {}

    with open("input.txt") as f:
        notesPg, yourTickPg, nearbyTickPg = f.read().strip().split("\n\n")

    for line in notesPg.split("\n"):
        a, b = line.split(": ")
        b1, b2 = b.split(" or ")
        r1 = range(int(b1.split("-")[0]), int(b1.split("-")[1]) + 1)
        r2 = range(int(b2.split("-")[0]), int(b2.split("-")[1]) + 1)
        validation[a] = set(r1) | set(r2)

    myTicket = list(map(int, yourTickPg.split("\n")[1].split(",")))
    n = len(myTicket)

    possibleLabels = {i: set(validation.keys()) for i in range(n)}
    for line in nearbyTickPg.split("\n")[1:]:
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


print(a(), b(), sep="\n")
