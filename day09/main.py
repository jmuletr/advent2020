preamble = 25
invalid_index = 0


def is_valid(index, numbers):
    values = numbers[index - preamble:index]
    for x in values:
        for y in values:
            if x + y == numbers[index]:
                return True
    return False


def find_first_invalid_number(numbers):
    global invalid_index
    index = preamble
    while index < len(numbers):
        if not is_valid(index, numbers):
            invalid_index = index
            return numbers[index]
        index += 1
    return "not found"


def find_contiguous_set(nums, targetNum):
    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums)):
            if sum(nums[k] for k in range(i, j)) == targetNum:
                return nums[i:j]


with open("input.txt") as f:
    numbers = [int(x.strip()) for x in f]

    print(find_first_invalid_number(numbers))
    contiguous_numbers = find_contiguous_set(numbers, numbers[invalid_index])
    print(min(contiguous_numbers) + max(contiguous_numbers))