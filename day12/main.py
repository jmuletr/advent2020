EAST = 'E'
WEST = 'W'
NORTH = 'N'
SOUTH = 'S'
FORWARD = 'F'
LEFT = 'L'
RIGHT = 'R'

directions = {
    EAST: (+1, 0),
    WEST: (-1, 0),
    NORTH: (0, +1),
    SOUTH: (0, -1),
}


def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])


def right_rotation(position, degree):
    x, y = position
    if degree % 360 == 0:
        return x, y
    elif degree % 360 == 90:
        return y, -x
    elif degree % 360 == 180:
        return -x, -y
    elif degree % 360 == 270:
        return -y, x
    else:
        raise ValueError('Degree not supported')


def left_rotation(position, degree):
    return right_rotation(position, 360 - degree)


def get_waypoint(waypoint, action, value):
    return (
        waypoint[0] + directions[action][0] * value,
        waypoint[1] + directions[action][1] * value,
    )


def go_forward(coord, direction, value):
    return (
        coord[0] + direction[0] * value,
        coord[1] + direction[1] * value,
    )


def go_direction(coord, direction, value):
    return (
        coord[0] + directions[direction][0] * value,
        coord[1] + directions[direction][1] * value,
    )


def get_part_1_distance(instructions):
    dr = directions[EAST]
    coord = (0, 0)

    for action, value in instructions:
        if action == FORWARD:
            coord = go_forward(coord, dr, value)
        elif action in directions.keys():
            coord = go_direction(coord, action, value)
        elif action == LEFT:
            dr = left_rotation(dr, value)
        elif action == RIGHT:
            dr = right_rotation(dr, value)

    return manhattan_distance(coord)


def get_part_2_distance(instructions):
    coord = (0, 0)
    waypoint = (+10, +1)

    for action, value in instructions:
        if action == FORWARD:
            coord = go_forward(coord, waypoint, value)
        elif action in directions.keys():
            waypoint = get_waypoint(waypoint, action, value)
        elif action == LEFT:
            waypoint = left_rotation(waypoint, value)
        elif action == RIGHT:
            waypoint = right_rotation(waypoint, value)

    return manhattan_distance(coord)


def extract_data(lines):
    data = []
    for line in lines:
        action = line[:1]
        value = int(line[1:])
        data.append((action, value))
    return data


with open("input.txt") as f:
    lines = [x.strip() for x in f]

    print(get_part_1_distance(extract_data(lines)))
    print(get_part_2_distance(extract_data(lines)))
