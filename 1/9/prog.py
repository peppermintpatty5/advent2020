#!/usr/bin/env python3

import sys


def getRules(inputTxt: str) -> dict:
    rules = {}
    for line in inputTxt.splitlines():
        if line == "":
            break
        a, b = line.split(": ")
        key = int(a)
        val = {
            tuple(t[1:-1] if t.startswith('"') else int(t) for t in s.split(" "))
            for s in b.split(" | ")
        }
        rules[key] = val
    return rules


def derive(rules: dict, start: tuple, expr: str) -> bool:
    if start == () or expr == "":
        return len(start) == len(expr)

    lhs = start[0]
    if type(lhs) is str:
        return lhs == expr[0] and derive(rules, start[1:], expr[1:])
    else:
        for rhs in rules[lhs]:
            if derive(rules, rhs + start[1:], expr):
                return True
    return False


def a(inputTxt: str) -> int:
    lines = inputTxt.splitlines()
    rules = getRules(inputTxt)
    messages = lines[lines.index("") + 1 :]

    return sum(1 for msg in messages if derive(rules, (0,), msg))


def b(inputTxt: str) -> int:
    lines = inputTxt.splitlines()
    rules = getRules(inputTxt)
    messages = lines[lines.index("") + 1 :]

    rules[8] = {(42,), (42, 8)}
    rules[11] = {(42, 31), (42, 11, 31)}

    return sum(1 for msg in messages if derive(rules, (0,), msg))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
