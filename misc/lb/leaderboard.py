#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Any

import tabulate


YEAR = 2020


def dictMultiGet(d: dict, *keys: Any, default=None) -> Any:
    """
    If `d` is a nested dictionary and `keys = [k1, k2, ..., kn]`, returns the
    equivalent to `d[k1][k2]...[kn]`.
    """
    for key in keys:
        if d is None:
            return default
        else:
            d = d.get(key, None)

    return d


def getTimes(stats: dict, day: int) -> dict:
    """
    Returns dictionary of completion times, mapping each member ID to a pair of
    `timedelta` objects. The pair corresponds to parts 1 and 2 of the puzzle.

    If player did not complete the puzzle, time will be `None`.
    """
    times = {}
    dayStart = datetime(YEAR, 12, day, 5)  # hour=5 for EST timezone

    for memID, member in stats["members"].items():
        x = dictMultiGet(member, "completion_day_level", str(day))
        ts1 = dictMultiGet(x, "1", "get_star_ts")
        ts2 = dictMultiGet(x, "2", "get_star_ts")

        time1 = (
            datetime.utcfromtimestamp(int(ts1)) - dayStart if ts1 is not None else None
        )
        time2 = (
            datetime.utcfromtimestamp(int(ts2)) - dayStart if ts2 is not None else None
        )
        times[memID] = (time1, time2)

    return times


def getScores(times: dict) -> dict:
    """
    Returns dictionary of scores, mapping each member ID to a pair of integers.
    The pair corresponds to parts 1 and 2 of the puzzle.

    If player did not complete the puzzle, score will be `0`.
    """
    n = len(times)
    ranks1 = sorted(
        (memID for memID in times if times[memID][0] is not None),
        key=lambda memID: times[memID][0],
    )
    ranks2 = sorted(
        (memID for memID in times if times[memID][1] is not None),
        key=lambda memID: times[memID][1],
    )

    scores1 = {}
    scores2 = {}
    for i, memID in enumerate(ranks1):
        scores1[memID] = n - i
    for i, memID in enumerate(ranks2):
        scores2[memID] = n - i

    return {memID: (scores1.get(memID, 0), scores2.get(memID, 0)) for memID in times}


def aocTimeFormat(td: timedelta) -> str:
    """
    Formats `td` like `H:MM:SS`, which is the default format. If `td` is
    greater than 1 day, returns `>24h`.
    """
    return format(td) if td < timedelta(days=1) else ">24h"


def getRankTbl(stats: dict, day: int) -> list:
    """
    Returns list of rows, ordered by score, where each row contains
    `[memID, (time1, time2), (score1, score2)]`.
    """
    times = getTimes(stats, day)
    scores = getScores(times)

    return [
        [memID, times[memID], scores[memID]]
        for memID in sorted(scores, key=lambda memID: sum(scores[memID]), reverse=True)
    ]


def printDailyRankTbl(stats: dict, day: int) -> None:
    """
    Prints formatted table containing ranking information for the particular
    day (non-cumulative).
    """
    tblRows = []
    for i, [memID, (time1, time2), (score1, score2)] in enumerate(
        getRankTbl(stats, day)
    ):
        name = stats["members"][memID]["name"] or f"(anonymous user #{memID})"
        f_time1 = aocTimeFormat(time1) if time1 is not None else "-"
        f_time2 = aocTimeFormat(time2) if time2 is not None else "-"
        tblRows.append([i + 1, score1, score2, f_time1, f_time2, name])

    print(
        tabulate.tabulate(
            tblRows,
            headers=["Rank", "Score 1", "Score 2", "Time 1", "Time 2", "Username"],
        )
    )


def main():
    parser = argparse.ArgumentParser(
        description="""
        Simple leaderboard calculator for Advent of Code. Input should be the
        JSON file downloaded from your leaderboard webpage.
        """
    )
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    stats = json.load(sys.stdin)
    printDailyRankTbl(stats, args.day)


if __name__ == "__main__":
    main()
