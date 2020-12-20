#!/usr/bin/env python3

import sys


def run(prog: list) -> tuple:
    i = 0
    acc = 0
    dups = set()

    while i < len(prog):
        if i in dups:
            return acc, False
        else:
            dups.add(i)

        instr, val = prog[i]
        val = int(val)

        if instr == "acc":
            acc += val
        elif instr == "jmp":
            i += val
            continue
        elif instr == "nop":
            pass

        i += 1
    return acc, True


def a(inputTxt: str) -> int:
    prog = [line.split(" ") for line in inputTxt.splitlines()]
    acc, halt = run(prog)

    return acc


def b(inputTxt: str) -> int:
    prog = [line.split(" ") for line in inputTxt.splitlines()]

    for i in range(len(prog)):
        instr, val = prog[i]
        if instr == "jmp" or instr == "nop":
            prog[i][0] = "jmp" if instr == "nop" else "nop"
        else:
            continue

        acc, halt = run(prog)
        if halt:
            return acc
        else:  # change back
            prog[i][0] = instr


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
