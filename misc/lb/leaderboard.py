#!/usr/bin/env python3

import argparse
import json
import sys
from datetime import datetime, timezone
from typing import Any

import tabulate


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


def getStarTimes(stats: dict, day: int) -> dict:
    """
    Returns dictionary of star completion times, mapping member ID to a pair of
    `datetime` objects. The pair corresponds to part 1 and 2 of each puzzle.

    A time will be `None` if there was no completion time.
    """
    starTimes = {}

    for memID, member in stats["members"].items():
        x = dictMultiGet(member, "completion_day_level", str(day))
        t1 = dictMultiGet(x, "1", "get_star_ts")
        t2 = dictMultiGet(x, "2", "get_star_ts")

        starTimes[memID] = (
            datetime.utcfromtimestamp(int(t1)) if t1 is not None else None,
            datetime.utcfromtimestamp(int(t2)) if t2 is not None else None,
        )

    return starTimes


def getPoints(starTimes: dict) -> dict:
    """
    Given a dictionary of star completion times, awards points based on the
    order in which both parts were completed.
    """
    points = {}
    n = len(starTimes)
    r1 = sorted(starTimes, key=lambda memID: starTimes[memID][0] or datetime.now())
    r2 = sorted(starTimes, key=lambda memID: starTimes[memID][1] or datetime.now())

    for i, memID in enumerate(r1):
        points[memID] = n - i if starTimes[memID][0] is not None else 0
    for i, memID in enumerate(r2):
        points[memID] += n - i if starTimes[memID][0] is not None else 0

    return points


def printDailyRankTbl(stats: dict, day: int) -> None:
    """
    Prints formatted table containing ranking information for the particular
    day (non-cumulative).
    """
    starTimes = getStarTimes(stats, day)
    points = getPoints(starTimes)

    tblRows = []
    for i, memID in enumerate(
        sorted(points, key=lambda memID: points[memID], reverse=True)
    ):
        member = stats["members"][memID]
        name = (
            member["name"]
            if member["name"] is not None
            else f"(anonymous user #{memID})"
        )
        stars = "".join("*" if x is not None else " " for x in starTimes[memID])
        tblRows.append([i + 1, points[memID], stars, name])
    print(tabulate.tabulate(tblRows, headers=["Rank", "Points", "Stars", "Username"]))


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
