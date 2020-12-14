#!/usr/bin/env python3


def a():
    mem = {}
    with open("input.txt") as f:
        for line in f:
            a, b = line.strip().split(" = ")
            if a == "mask":
                orMask = int(b.replace("X", "0"), base=2)
                andMask = int(b.replace("X", "1"), base=2)
            else:
                addr = int(a[4:-1])
                val = (int(b) | orMask) & andMask
                mem[addr] = val
    return sum(mem.values())


def boolIter(n):
    return (tuple(c == "1" for c in bin(i)[2:].zfill(n)) for i in range(1 << n))


def combinate(addr: str) -> list:
    combos = []
    indices = [i for i, c in enumerate(addr) if c == "X"]

    for x in boolIter(len(indices)):
        flips = {indices[i] for i, b in enumerate(x) if b}
        combos.append(
            int(
                "".join(
                    b if b != "X" else ("1" if i in flips else "0")
                    for i, b in enumerate(addr)
                ),
                base=2,
            )
        )
    return combos


def b():
    mem = {}
    with open("input.txt") as f:
        for line in f:
            a, b = line.strip().split(" = ")
            if a == "mask":
                mask = b
            else:
                val = int(b)

                addr = bin(int(a[4:-1]))[2:].zfill(36)
                addr = "".join(
                    m if m == "1" else a if m == "0" else "X"
                    for a, m in zip(addr, mask)
                )
                for combo in combinate(addr):
                    mem[combo] = val
    return sum(mem.values())


print(a(), b(), sep="\n")
