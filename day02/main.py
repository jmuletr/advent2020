from collections import Counter

def solvePart1(lines):
    global part1
    for line in lines:
        chunks = line.split()
        minAndMax = chunks[0].split("-")
        min, max = int(minAndMax[0]), int(minAndMax[1])
        c = chunks[1][0]
        passwd = chunks[2]

        counts = Counter(passwd)[c]
        if min <= counts <= max:
            part1 += 1

        solvePart2(c, passwd, min, max)

def solvePart2(character, passwd, min, max):
    global part2
    correct_pos1, correct_pos2 = passwd[min - 1], passwd[max - 1]
    if (character == correct_pos1) ^ (character == correct_pos2):
        part2 += 1

with open("input.txt") as file:
    lines = [x.strip() for x in file]
    part1 = 0
    part2 = 0

    solvePart1(lines)
    print(part1)
    print(part2)





