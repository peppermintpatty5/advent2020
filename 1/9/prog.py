#!/usr/bin/env python3


def getRules(ruleInput: str) -> dict:
    rules = {}
    for line in ruleInput.split("\n"):
        if line == "":
            continue
        a, b = line.split(": ")
        key = int(a)
        val = {
            s[1:-1] if s.startswith('"') else tuple(map(int, s.split(" ")))
            for s in b.split(" | ")
        }
        rules[key] = val
    return rules


def derive(rules: dict, start: tuple, expr: str) -> bool:
    if start == () or expr == "":
        return len(start) == len(expr)

    for rhs in rules[start[0]]:
        if type(rhs) is str:
            if rhs == expr[0]:
                return derive(rules, start[1:], expr[1:])
        else:
            expand = rhs + start[1:]
            if derive(rules, expand, expr):
                return True
    return False


def a():
    with open("input.txt") as f:
        ruleInput, messages = f.read().strip().split("\n\n")
    rules = getRules(ruleInput)

    return sum(1 for line in messages.split("\n") if derive(rules, (0,), line))


def b():
    with open("input.txt") as f:
        ruleInput, messages = f.read().strip().split("\n\n")
    rules = getRules(ruleInput)

    rules[8] = {(42,), (42, 8)}
    rules[11] = {(42, 31), (42, 11, 31)}

    return sum(1 for line in messages.split("\n") if derive(rules, (0,), line))


print(a(), b(), sep="\n")
