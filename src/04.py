#!/usr/bin/env python3

import sys


def getPassports(inputTxt: str) -> list:
    passports = []
    p = {}

    for line in inputTxt.splitlines():
        if line == "":
            passports.append(p)
            p = {}
        else:
            for field in line.split(" "):
                key, val = field.split(":")
                p[key] = val
    passports.append(p)

    return passports


def allKeys(d: dict) -> bool:
    return all(k in d for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def a(inputTxt: str) -> int:
    passports = getPassports(inputTxt)

    return sum(1 for p in passports if allKeys(p))


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


def b(inputTxt: str) -> int:
    passports = getPassports(inputTxt)

    return sum(1 for p in passports if allKeys(p) and allVals(p))


def main():
    inputTxt = sys.stdin.read()
    print(a(inputTxt))
    print(b(inputTxt))


if __name__ == "__main__":
    main()
