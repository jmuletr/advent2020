decoded_ids = []
missing_seat = 0
lower_signs = ["F", "L"]
upper_signs = ["B", "R"]


def decode(minimum, maximum, code):
    for index in range(len(code)):
        mid = 1 + (maximum - minimum) // 2
        if code[index] in lower_signs:
            maximum = maximum - mid
        elif code[index] in upper_signs:
            minimum = minimum + mid
    return minimum


def decode_id(code):
    row = decode(0, 127, code[0:7])
    col = decode(0, 7, code[7:10])
    return row * 8 + col


def find_missing_seats():
    global missing_seat
    decoded_ids.sort()

    previous = decoded_ids[0]
    for i in range(1, len(decoded_ids)):
        if decoded_ids[i] - previous != 1:
            missing_seat = decoded_ids[i] - 1
            break
        else:
            previous = decoded_ids[i]


with open("input.txt") as f:
    lines = [x.strip() for x in f]

    for l in lines:
        decoded_ids.append(decode_id(l))

    find_missing_seats()

    print(max(decoded_ids))
    print(missing_seat)
