#!/usr/bin/env python3


def tokenize(expr: str):
    return (c if c in "+*()" else int(c) for c in expr if not c.isspace())


def shuntingYard(infixExpr: str, precedence: dict) -> list:
    """Credit to Wikipedia and Edsger Dijkstra"""

    output = []
    operators = []
    tokenStream = tokenize(infixExpr)

    while True:
        try:
            token = next(tokenStream)
        except StopIteration as e:
            break

        if type(token) is int:
            output.append(token)
        elif token in "+*":
            while (
                len(operators) > 0
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[token]
            ):
                output.append(operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while len(operators) > 0 and operators[-1] != "(":
                output.append(operators.pop())
            if len(operators) > 0 and operators[-1] == "(":
                operators.pop()

    while len(operators) > 0:
        output.append(operators.pop())

    return output


def evaluate(infixExpr: str, precedence: dict) -> int:
    stack = []
    operatorFunc = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}

    for token in shuntingYard(infixExpr, precedence):
        if type(token) is int:
            stack.append(token)
        else:
            stack.append(operatorFunc[token](stack.pop(), stack.pop()))
    return stack.pop()


def a():
    with open("input.txt") as f:
        exprList = [line.strip() for line in f]

    return sum(evaluate(expr, {"+": 1, "*": 1}) for expr in exprList)


def b():
    with open("input.txt") as f:
        exprList = [line.strip() for line in f]

    return sum(evaluate(expr, {"+": 2, "*": 1}) for expr in exprList)


print(a(), b(), sep="\n")
