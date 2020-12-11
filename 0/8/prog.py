#!/usr/bin/env python3


def a():
    with open("input.txt") as f:
        prog = [line.strip().split(" ") for line in f]

    acc = 0
    i = 0
    dups = set()
    while i < len(prog):
        if i in dups:
            return acc
        else:
            dups.add(i)

        instr, val = prog[i]
        val = int(val)

        if instr == "acc":
            acc += val
        elif instr == "jmp":
            i += val
            continue
        else:
            pass

        i += 1


def run(prog: list) -> int:
    acc = 0
    i = 0
    dups = set()
    while i < len(prog):
        if i in dups:
            return None
        else:
            dups.add(i)

        instr, val = prog[i]
        val = int(val)

        if instr == "acc":
            acc += val
        elif instr == "jmp":
            i += val
            continue
        else:
            pass

        i += 1
    return acc


def willHalt(prog: list) -> bool:
    return run(prog) is not None


def b():
    with open("input.txt") as f:
        prog = [line.strip().split(" ") for line in f]

    for i in range(len(prog)):
        instr, val = prog[i]
        if instr == "jmp" or instr == "nop":
            prog[i][0] = "jmp" if instr == "nop" else "nop"
        else:
            continue

        if willHalt(prog):
            return run(prog)
        else:  # change back
            prog[i][0] = instr


print(a(), b(), sep="\n")
