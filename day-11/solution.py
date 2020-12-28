"""
--- Day 11: Seating System ---
Definitely not optimized solutions, but they solve the problem!
TODO: find more optimized solutions
"""
import copy


_INITIAL_SEATS = []
_CHART_WIDTH = 0
_CHART_HEIGHT = 0

# the key is the direction, value is the coordinate change it actually represents
_DIRECTIONS_DICT = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1)
}

def look_direction(direction, current_x, current_y, seats_chart):
    """
    Helper function that keeps going in a specific direction until we find a chair,
    then returns if that's occupied or not
    TRUE = OCCUPIED SEAT FOUND
    FALSE = UNOCCUPIED SEAT FOUND
    """
    if (0 <= (iter_x := current_x + direction[0]) < _CHART_WIDTH) is False:
        return False

    if (0 <= (iter_y := current_y + direction[1]) < _CHART_HEIGHT) is False:
        return False

    while True:
        looking_spot = seats_chart[iter_y][iter_x]
        if looking_spot == "#":
            return True

        if looking_spot == "L":
            return False

        iter_x += direction[0]
        iter_y += direction[1]

        if iter_x < 0 or iter_y < 0 or iter_x == _CHART_WIDTH or iter_y == _CHART_HEIGHT:
            return False


def puzzle2():
    """
    Solution for puzzle 2, rule is changed that we keep looking in a direction until
    we find a seat, occupied or not + tolerance is up to 5 neighbors
    """
    seats = copy.deepcopy(_INITIAL_SEATS)
    next_seats = copy.deepcopy(seats)

    stablized = False

    while stablized is False:
        seats_shuffled = False
        for y_2 in range(_CHART_HEIGHT):
            for x_2 in range(_CHART_WIDTH):
                current_spot = seats[y_2][x_2]
                if current_spot != ".":
                    occupied = 0
                    for direction in _DIRECTIONS_DICT:
                        is_occupied = look_direction(_DIRECTIONS_DICT[direction], x_2, y_2, seats)
                        if is_occupied:
                            occupied += 1
                    if occupied >= 5 and current_spot == "#":
                        seats_shuffled = True
                        next_seats[y_2][x_2] = "L"
                    elif occupied == 0 and current_spot == "L":
                        seats_shuffled = True
                        next_seats[y_2][x_2] = "#"
        if seats_shuffled is False:
            stablized = True

        seats = copy.deepcopy(next_seats)

    total = 0
    for row in seats:
        for spot in row:
            if spot == "#":
                total += 1
    return total


def find_neighbors(current_x, current_y):
    """
    Helper function that returns the combinations of coordinates of the neighbors
    for the current square we're checking
    """
    x_range = []
    y_range = []

    if current_x == 0:
        x_range = [current_x, current_x + 1]
    elif current_x > 0 and current_x != _CHART_WIDTH - 1:
        x_range = [current_x - 1, current_x, current_x + 1]
    elif current_x == _CHART_WIDTH - 1:
        x_range = [current_x - 1, current_x]

    if current_y == 0:
        y_range = [current_y, current_y + 1]
    elif current_y > 0 and current_y != _CHART_HEIGHT - 1:
        y_range = [current_y - 1, current_y, current_y + 1]
    elif current_y == _CHART_HEIGHT - 1:
        y_range = [current_y - 1, current_y]

    neighbors = [(x, y) for x in x_range for y in y_range]
    neighbors.remove((current_x, current_y)) #remove the actual one we're looking at
    return neighbors


def puzzle1():
    """
    Solution for puzzle 1
    This puzzle is essentially John Conway's Game of Life, with simpler rules but
    needs to account for the empty floor spaces.
    """
    seat_chart = copy.deepcopy(_INITIAL_SEATS)
    next_iteration = copy.deepcopy(seat_chart)

    stable_seating = False

    while stable_seating is False:
        seats_changed = False
        for my_y in range(_CHART_HEIGHT):
            for my_x in range(_CHART_WIDTH):
                if seat_chart[my_y][my_x] != ".":
                    current_neighbors = find_neighbors(my_x, my_y)
                    occupied_surround = 0
                    for neighbor in current_neighbors:
                        spot = seat_chart[neighbor[1]][neighbor[0]]
                        if spot == "#":
                            occupied_surround += 1
                    if occupied_surround >= 4 and seat_chart[my_y][my_x] == "#":
                        next_iteration[my_y][my_x] = "L"
                        seats_changed = True
                    elif occupied_surround == 0 and seat_chart[my_y][my_x] == "L":
                        next_iteration[my_y][my_x] = "#"
                        seats_changed = True

        if seats_changed is False:
            stable_seating = True
        seat_chart = copy.deepcopy(next_iteration)

    final_headcount = 0
    for row in seat_chart:
        for spot in row:
            if spot == "#":
                final_headcount += 1
    return final_headcount


if __name__ == "__main__":
    with open("input.txt") as file:
        _INITIAL_SEATS = [list(line) for line in file.read().splitlines()]
        _CHART_WIDTH = len(_INITIAL_SEATS[0])
        _CHART_HEIGHT = len(_INITIAL_SEATS)

    FINAL_OCCUPIED = puzzle1()
    print(FINAL_OCCUPIED)

    FINAL_2 = puzzle2()
    print(FINAL_2)
