#!/usr/bin/env python3


def a():
    count = 0
    s = set()
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                count += len(s)
                s.clear()
            else:
                for c in line:
                    s.add(c)
    return count + len(s)


def b():
    count = 0
    l = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                count += len(set.intersection(*l))
                l.clear()
            else:
                l.append(set(line))
    return count + len(set.intersection(*l))


print(a(), b(), sep="\n")
