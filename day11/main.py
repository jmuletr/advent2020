import copy

directions = [(+1, 0), (-1, 0), (0, +1), (0, -1), (-1, -1), (+1, -1), (+1, +1), (-1, +1)]

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'


def number_of_occupied_seats(layout):
    count = 0
    for row in layout:
        count += row.count(OCCUPIED_SEAT)
    return count


def number_of_occupied_immediately_adjacent_seats(layout, row_ix, col_ix):
    count = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, col_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + col_dir
        if (0 <= rix < row_len) and (0 <= cix < col_len) and (layout[rix][cix] == OCCUPIED_SEAT):
            count += 1
    return count


def number_of_occupied_first_next_seats(layout, row_ix, col_ix):
    count = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, col_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + col_dir
        while (0 <= rix < row_len) and (0 <= cix < col_len):
            if layout[rix][cix] == EMPTY_SEAT:
                break
            if layout[rix][cix] == OCCUPIED_SEAT:
                count += 1
                break
            rix += row_dir
            cix += col_dir
    return count


def run_rules(initial_layout, tolerance_lvl, use_immediately_adjacent_seats):
    prev_layout = []
    layout = copy.deepcopy(initial_layout)

    while layout != prev_layout:
        prev_layout = copy.deepcopy(layout)
        layout = []

        for row_ix, prev_row in enumerate(prev_layout):
            row = ''

            for col_ix, prev_position in enumerate(prev_row):
                if use_immediately_adjacent_seats:
                    num = number_of_occupied_immediately_adjacent_seats(prev_layout, row_ix, col_ix)
                else:
                    num = number_of_occupied_first_next_seats(prev_layout, row_ix, col_ix)

                if num == 0 and prev_position == EMPTY_SEAT:
                    row += OCCUPIED_SEAT
                elif num >= tolerance_lvl and prev_position == OCCUPIED_SEAT:
                    row += EMPTY_SEAT
                else:
                    row += prev_position

            layout.append(row)

    return layout


with open("input.txt") as f:
    lines = [line for line in f.read().splitlines()]

    print(number_of_occupied_seats(run_rules(lines, 4, True)))
    print(number_of_occupied_seats(run_rules(lines, 5, False)))
