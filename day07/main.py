def contains(rules, key):
    if 'no other' in rules[key]:
        return False

    if 'shiny gold' in rules[key]:
        return True

    bags = rules[key].split(', ')
    colors = []
    for x in bags:
        y = x.split(' ')
        colors.append(y[1] + ' ' + y[2])

    for x in colors:
        if contains(rules, x):
            return True

    return False


def count_bags(rules, key):
    if 'no other' in rules[key]:
        return 0

    bags = rules[key].split(', ')
    count = 0
    for x in bags:
        y = x.split(' ')
        count += int(y[0]) + (int(y[0]) * count_bags(rules, y[1] + ' ' + y[2]))

    return count


with open("input.txt") as f:
    lines = f.read().split('\n')

dictionary_results = {}
for i in lines:
    values = i.split(' contain ')
    if len(values) > 1:
        dictionary_results[values[0][:-5]] = values[1]

counter = 0
for x in dictionary_results.keys():
    if contains(dictionary_results, x):
        counter += 1

print(counter)
print(count_bags(dictionary_results, 'shiny gold'))
