from collections import Counter


def findDif(last_number, adapters):
    dif = []
    for adapter in adapters:
        dif.append(adapter - last_number)
        last_number = adapter
    return dif


def find_number_of_combinations(adapters):
    dp = Counter()
    dp[0] = 1

    for adapter in adapters:
        dp[adapter] = dp[adapter - 1] + dp[adapter - 2] + dp[adapter - 3]

    return dp[adapters[-1]]


with open("input.txt") as f:
    adapters = sorted([int(x.strip()) for x in f])
    adapters.append(max(adapters) + 3)

    dif_values = findDif(0, adapters)
    result = dif_values.count(1) * (dif_values.count(3))
    print(result)
    print(find_number_of_combinations(adapters))
