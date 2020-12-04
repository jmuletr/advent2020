import re

expected = set("byr iyr eyr hgt hcl ecl pid".split())
passports = []
valids1 = 0
valids2 = 0


def get_passports():
    global passports
    counter = 0
    while counter < len(lines):
        k = ""
        while len(lines[counter]) > 0:
            k += " " + lines[counter]
            counter += 1
            if counter == len(lines):
                break
        passports.append(k)
        counter += 1


def validate_height(hgt):
    if "cm" in hgt:
        return 150 <= int(hgt.split("cm")[0]) <= 193
    elif "in" in hgt:
        return 59 <= int(hgt.split("in")[0]) <= 76
    else:
        return False


def validate_passports():
    global valids1, valids2
    for p in passports:
        chunks = p.split()
        keys = set([c.split(":")[0] for c in chunks])
        if len(expected - keys) == 0:
            valids1 += 1
            data = dict([c.split(":") for c in chunks])
            byr = len(data["byr"]) == 4 and 1920 <= int(data["byr"]) <= 2002
            iyr = len(data["iyr"]) == 4 and 2010 <= int(data["iyr"]) <= 2020
            eyr = len(data["eyr"]) == 4 and 2020 <= int(data["eyr"]) <= 2030
            hgt = validate_height(data["hgt"])
            hcl = re.match(r"^#[a-f0-9]{6}", data["hcl"])
            ecl = data["ecl"] in "amb blu brn gry grn hzl oth"
            pid = len(data["pid"]) == 9 and data["pid"].isnumeric()
            if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
                valids2 += 1


with open("input.txt") as f:
    lines = [x.strip() for x in f]

    get_passports()
    validate_passports()

    print(valids1)
    print(valids2)
