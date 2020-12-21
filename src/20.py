#!/usr/bin/env python3

import sys
from math import sqrt


def splitList(l: list, sep, limit=-1) -> list:
    """
    Split a list into sub-lists using the given separator item.
    """
    i = -1
    subLists = []

    while limit < 0 or len(subLists) < limit:
        try:
            j = l.index(sep, i + 1)
        except ValueError as e:
            break

        subLists.append(l[i + 1 : j])
        i = j

    subLists.append(l[i + 1 :])
    return subLists


def getTiles(inputTxt: str) -> dict:
    """
    Given the puzzle input, returns a dictionary that maps tile ID#'s to tiles.
    Each tile is a list of single-line strings.
    """
    tiles = {}
    for s in splitList(inputTxt.splitlines(), ""):
        tileId = int(s[0].split(" ")[1][:-1])
        tile = s[1:]
        tiles[tileId] = tile
    return tiles


def borderCombos(tile: list) -> list:
    """
    Each tile has 8 border combinations: 4 sides * 2 mirrors per side. Borders
    are represented as single-line strings.
    """
    x = tile
    combos = []
    for i in range(4):
        combos.append(x[0])
        combos.append(x[0][::-1])
        x = rotate_cw(x)
    return combos


def getBorders(tiles: dict) -> dict:
    """
    Given a dictionary of tiles (see `getTiles`), returns a dictionary that
    maps borders to lists of corresponding tile ID#'s.
    """
    borders = {}
    for tileId, tile in tiles.items():
        for b in borderCombos(tile):
            if b in borders:
                borders[b].append(tileId)
            else:
                borders[b] = [tileId]
    return borders


def isUnpaired(b: str, borders: dict):
    return len(borders[b]) == 1


def countUnpaired(borders: dict) -> dict:
    """
    Given a dictionary of borders (see `getBorders`), returns a dictionary that
    maps tile ID#'s to integers counting the number of unpaired borders.
    """
    unpaired = {}
    for b, tileIdList in borders.items():
        if len(tileIdList) == 1:
            tileId = tileIdList[0]
            if tileId in unpaired:
                unpaired[tileId] += 1
            else:
                unpaired[tileId] = 1
    # due to mirroring in borderCombos, counts need to be halved
    return {tileId: count // 2 for tileId, count in unpaired.items()}


def arrange(tiles: dict) -> list:
    """
    The heavy lifting. Assumes that every tile pairs with exactly 1 other tile.
    """
    borders = getBorders(tiles)
    unpaired = countUnpaired(borders)
    corners = {tileId for tileId, count in unpaired.items() if count == 2}

    n = int(sqrt(len(tiles)))
    idLayout = [[None for c in range(n)] for r in range(n)]
    tileLayout = [[None for c in range(n)] for r in range(n)]

    # does not matter which corner to start with
    xi = list(corners)[0]
    x = tiles[xi]
    # rotate x such that top border is unpaired
    while not isUnpaired(x[0], borders):
        x = rotate_cw(x)
    # flip x such that left border is unpaired
    if not isUnpaired(rotate_cw(x)[0], borders):
        x = flip_horz(x)
    # put x in top-left of layout
    idLayout[0][0] = xi
    tileLayout[0][0] = x

    for r in range(n):
        if r != 0:  # already positioned tile at (0, 0)
            aboveId = idLayout[r - 1][0]
            aboveTile = tileLayout[r - 1][0]
            # bottom border of above tile
            bb = aboveTile[-1][::-1]
            # hopefully there is only 1 other tile that matches
            hope = [tileId for tileId in borders[bb] if tileId != aboveId]
            xi = hope[0] if len(hope) == 1 else None
            x = tiles[xi]
            # orient x such that its top border matches bb
            while x[0] != bb and x[0] != bb[::-1]:
                x = rotate_cw(x)
            if x[0] != bb[::-1]:
                x = flip_horz(x)
            # put x in the grid
            idLayout[r][0] = xi
            tileLayout[r][0] = x

        for c in range(1, n):
            leftId = idLayout[r][c - 1]
            leftTile = tileLayout[r][c - 1]
            # right border of left tile
            rb = rotate_ccw(leftTile)[0]
            # hopefully there is only 1 other tile that matches
            hope = [tileId for tileId in borders[rb] if tileId != leftId]
            xi = hope[0] if len(hope) == 1 else None
            x = tiles[xi]
            # orient x such that its left border matches rb
            while x[0] != rb and x[0] != rb[::-1]:
                x = rotate_cw(x)
            if x[0] != rb[::-1]:
                x = flip_horz(x)
            x = rotate_ccw(x)
            # put x in the grid
            idLayout[r][c] = xi
            tileLayout[r][c] = x

    return tileLayout


def rotate_cw(tile: list) -> list:
    n = len(tile)
    rot = [[None for c in range(n)] for r in range(n)]

    for r in range(n):
        for c in range(n):
            rot[c][n - r - 1] = tile[r][c]

    return ["".join(line) for line in rot]


def rotate_ccw(tile: list) -> list:
    n = len(tile)
    rot = [[None for c in range(n)] for r in range(n)]

    for r in range(n):
        for c in range(n):
            rot[r][c] = tile[c][n - r - 1]

    return ["".join(line) for line in rot]


def flip_horz(tile: list) -> list:
    return [row[::-1] for row in tile]


def flip_vert(tile: list) -> list:
    return tile[::-1]


def trim_borders(tile: list) -> list:
    return [row[1:-1] for row in tile[1:-1]]


def a(inputTxt: str) -> int:
    tiles = getTiles(inputTxt)
    borders = getBorders(tiles)
    unpaired = countUnpaired(borders)
    # corner tiles have 2 unpaired borders
    corners = {tileId for tileId, count in unpaired.items() if count == 2}

    product = 1
    for tileId in corners:
        product *= tileId
    return product


def reMatch(search: str, expr: str) -> bool:
    """
    Crude, regular-expression-like matching function, specifically for sea
    monsters.
    """
    for s, e in zip(search, expr):
        if s != " " and s != e:
            return False
    return True


def countMonsters(image: list):
    n = len(image)
    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    h = len(monster)
    w = len(monster[0])

    count = 0
    for r in range(n - h):
        for c in range(n - w):
            if all(reMatch(monster[i], image[r + i][c : c + w]) for i in range(h)):
                count += 1
    return count


def b(inputTxt: str) -> int:
    tiles = getTiles(inputTxt)
    layout = arrange(tiles)

    image = []
    for row in layout:
        for z in zip(*(trim_borders(tile) for tile in row)):
            image.append("".join(z))

    for _ in range(4):
        count = countMonsters(image)
        if count == 0:
            image = rotate_cw(image)
        else:
            return sum(row.count("#") for row in image) - 15 * count
    image = flip_horz(image)
    for _ in range(4):
        count = countMonsters(image)
        if count == 0:
            image = rotate_cw(image)
        else:
            return sum(row.count("#") for row in image) - 15 * count


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
