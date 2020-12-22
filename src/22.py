#!/usr/bin/env python3

import sys


def getDecks(inputTxt: str) -> tuple:
    player1 = []
    player2 = []
    currDeal = player1
    for line in inputTxt.splitlines():
        if line == "":
            currDeal = player2
        else:
            if line.isnumeric():
                currDeal.append(int(line))
    return player1, player2


def a(inputTxt: str) -> int:
    player1, player2 = getDecks(inputTxt)

    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1 += [card1, card2]
        else:
            player2 += [card2, card1]

    winner = player1 if len(player1) > 0 else player2
    n = len(winner)
    return sum((n - i) * c for i, c in enumerate(winner))


def playGame(player1: list, player2: list, depth=0) -> int:
    configs = set()

    while len(player1) > 0 and len(player2) > 0:
        config = (tuple(player1), tuple(player2))
        if config in configs:
            return 1
        else:
            configs.add(config)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if len(player1) >= card1 and len(player2) >= card2:
            roundWinner = playGame(player1[:card1], player2[:card2], depth + 1)
        else:
            roundWinner = 1 if card1 > card2 else 2

        if roundWinner == 1:
            player1 += [card1, card2]
        else:
            player2 += [card2, card1]

    gameWinner = 1 if len(player1) > 0 else 2
    if depth == 0:
        n = len(player1) + len(player2)
        return sum(
            (n - i) * c for i, c in enumerate(player1 if gameWinner == 1 else player2)
        )
    else:
        return gameWinner


def b(inputTxt: str) -> int:
    player1, player2 = getDecks(inputTxt)
    return playGame(player1, player2)


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
