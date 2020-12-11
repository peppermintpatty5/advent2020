#!/usr/bin/env python3


def allKeys(d: dict) -> bool:
    return all(k in d for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def a():
    count = 0
    with open("input.txt") as f:
        passports = f.read().split("\n\n")

    for p in passports:
        d = {}
        for field in p.split():
            k, v = field.split(":", 1)
            d[k] = v
        if allKeys(d):
            count += 1
    return count


def allVals(d: dict) -> bool:
    hgt = d["hgt"]
    hcl = d["hcl"]
    ecl = d["ecl"]
    pid = d["pid"]
    return (
        1920 <= int(d["byr"]) <= 2002
        and 2010 <= int(d["iyr"]) <= 2020
        and 2020 <= int(d["eyr"]) <= 2030
        and (
            (hgt.endswith("cm") and 150 <= int(hgt[:-2]) <= 193)
            or (hgt.endswith("in") and 59 <= int(hgt[:-2]) <= 76)
        )
        and (
            hcl.startswith("#")
            and len(hcl[1:]) == 6
            and all(c in "0123456789abcdef" for c in hcl[1:])
        )
        and ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        and (len(pid) == 9 and all(d in "0123456789" for d in pid))
    )


def b():
    count = 0
    with open("input.txt") as f:
        passports = f.read().split("\n\n")

    for p in passports:
        d = {}
        for field in p.split():
            k, v = field.split(":", 1)
            d[k] = v
        if allKeys(d) and allVals(d):
            count += 1
    return count


print(a(), b(), sep="\n")
