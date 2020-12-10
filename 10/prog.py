#!/usr/bin/env python3


def search(j: int, jolts: set):
    diff = [1, 2, 3]

    if len(jolts) > 0:
        for d in diff:
            if j + d in jolts:
                path = search(j + d, jolts - {j + d})
                if path is not None:
                    return [j] + path
        return None
    else:
        return [j]


def a():
    with open("input.txt") as f:
        jolts = set(map(int, f))

    path = search(0, jolts)
    ones = 0
    threes = 0
    for i in range(len(path) - 1):
        d = abs(path[i] - path[i + 1])
        if d == 1:
            ones += 1
        elif d == 3:
            threes += 1

    return ones * (threes + 1)


def pathCount(jolts: set) -> int:
    paths = {max(jolts): 1}  # number of paths from node to goal
    for j in sorted(jolts, reverse=True)[1:]:
        s = {j + 1, j + 2, j + 3} & jolts
        paths[j] = sum(paths.get(k, 0) for k in s)

    return sum(paths.get(k, 0) for k in [1, 2, 3])


def b():
    with open("input.txt") as f:
        jolts = set(map(int, f))

    return pathCount(jolts)


print(a(), b(), sep="\n")
