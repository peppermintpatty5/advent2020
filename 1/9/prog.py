#!/usr/bin/env python3


def getRules(ruleInput: str) -> dict:
    rules = {}
    for line in ruleInput.split("\n"):
        if line == "":
            continue
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


def a():
    with open("input.txt") as f:
        ruleInput, messages = f.read().split("\n\n")
    rules = getRules(ruleInput)

    return sum(1 for line in messages.split("\n") if derive(rules, (0,), line))


def b():
    with open("input.txt") as f:
        ruleInput, messages = f.read().split("\n\n")
    rules = getRules(ruleInput)

    rules[8] = {(42,), (42, 8)}
    rules[11] = {(42, 31), (42, 11, 31)}

    return sum(1 for line in messages.split("\n") if derive(rules, (0,), line))


print(a(), b(), sep="\n")
