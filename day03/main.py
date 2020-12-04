slopes = [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]]
results = []


def slope(dx, dy):
    with open("input.txt") as f:
        lines = [x.strip() for x in f]

    width = len(lines[0])
    x = 0
    y = 0
    crashes = 0
    while y < len(lines):
        if lines[y][x] == '#':
            crashes += 1
        x += dx
        y += dy
        x %= width

    return crashes


for x in slopes:
    results.append(slope(x[0], x[1]))

print(results[0])
print(results[0] * results[1] * results[2] * results[3] * results[4])
