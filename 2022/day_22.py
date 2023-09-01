import re
from dataclasses import dataclass
from collections.abc import Sequence

NO_TILE = " "
OPEN_TILE = "."
WALL_TILE = "#"
TURN_LEFT = "L"
TURN_RIGHT = "R"


def walk_flat(board, position, direction, steps):
    current_y, current_x = position
    for step in range(steps):
        previous_pos = current_y, current_x
        current_y, current_x = current_y + direction[0], current_x + direction[1]
        if not (0 <= current_y < len(board) and 0 <= current_x < len(board[current_y])) or board[current_y][current_x] == NO_TILE:
            while True:
                new_wrap_y, new_wrap_x = current_y - direction[0], current_x - direction[1]
                if 0 <= new_wrap_y < len(board) and 0 <= new_wrap_x < len(board[new_wrap_y]) and not board[new_wrap_y][new_wrap_x] == NO_TILE:
                    current_y, current_x = new_wrap_y, new_wrap_x
                else:
                    break
        if board[current_y][current_x] == WALL_TILE:
            return previous_pos
    return current_y, current_x


def rotate(current_direction, rotation):
    if rotation == TURN_RIGHT:
        return current_direction[1], -current_direction[0]
    else:
        return -current_direction[1], current_direction[0]


def get_password(position, direction):
    match direction:
        case (0, 1):
            direction_points = 0
        case (1, 0):
            direction_points = 1
        case (0, -1):
            direction_points = 2
        case _:
            direction_points = 3
    return 1000 * (position[0] + 1) + 4 * (position[1] + 1) + direction_points


@dataclass
class Edge:
    edge1: tuple[Sequence, Sequence]
    direction1: tuple[int, int]
    edge2: tuple[Sequence, Sequence]
    direction2: tuple[int, int]

    def is_on_edge(self, position, direction):
        if direction == self.direction1:
            if position[0] in self.edge1[0] and position[1] in self.edge1[1]:
                return True
        if direction == self.direction2:
            return position[0] in self.edge2[0] and position[1] in self.edge2[1]

    def walk_over_edge(self, position, direction):
        if direction == self.direction1 and position[0] in self.edge1[0] and position[1] in self.edge1[1]:
            start_edge = self.edge1
            dest_edge = self.edge2
            dest_direction = -self.direction2[0], -self.direction2[1]
        else:
            start_edge = self.edge2
            dest_edge = self.edge1
            dest_direction = -self.direction1[0], -self.direction1[1]

        indexes_on_edge = start_edge[0].index(position[0]), start_edge[1].index(position[1])
        if self.direction1[0] + self.direction2[0] and self.direction1[1] + self.direction2[1]:  # Check if the indexes should be swapped
            indexes_on_edge = indexes_on_edge[1], indexes_on_edge[0]

        return dest_edge[0][indexes_on_edge[0]], dest_edge[1][indexes_on_edge[1]], dest_direction


def walk_cube(board, edges, position, direction, steps):
    current_y, current_x = position
    for step in range(steps):
        new_y, new_x = current_y + direction[0], current_x + direction[1]
        new_direction = direction
        if not (0 <= new_y < len(board) and 0 <= new_x < len(board[new_y])) or board[new_y][new_x] == NO_TILE:
            current_position = (current_y, current_x)
            for edge in edges:
                if edge.is_on_edge(current_position, direction):
                    new_y, new_x, new_direction = edge.walk_over_edge(current_position, direction)
                    break
            else:
                print("Failed to find edge!")
        if board[new_y][new_x] == WALL_TILE:
            break
        else:
            current_y, current_x = new_y, new_x
            direction = new_direction
    return (current_y, current_x), direction


def main():
    board = []

    with open("day_22_input", "r") as f:
        for line in (x.rstrip() for x in f):
            if line:
                board.append(line)
            else:
                break
        instructions = [instr_str for instr_str in re.findall(r"(\d+|.)", next(f))]

    start_position = (0, board[0].index(OPEN_TILE))
    position = start_position
    direction = (0, 1)

    for instruction in instructions:
        try:
            position = walk_flat(board, position, direction, int(instruction))
        except ValueError:
            direction = rotate(direction, instruction)
    print(get_password(position, direction))

    position = start_position
    direction = (0, 1)
    edges = (
        Edge(([0], range(50, 100)), (-1, 0),  # Edge between 1 and 6
             (range(150, 200), [0]), (0, -1)),
        Edge(([0], range(100, 150)), (-1, 0),  # Edge between 2 and 6
             ([199], range(0, 50)), (1, 0)),
        Edge((range(0, 50), [50]), (0, -1),  # Edge between 1 and 5
             (range(149, 99, -1), [0]), (0, -1)),
        Edge((range(0, 50), [149]), (0, 1),  # Edge between 2 and 4
             (range(149, 99, -1), [99]), (0, 1)),
        Edge(([49], range(100, 150)), (1, 0),  # Edge between 2 and 3
             (range(50, 100), [99]), (0, 1)),
        Edge((range(50, 100), [50]), (0, -1),  # Edge between 3 and 5
             ([100], range(0, 50)), (-1, 0)),
        Edge(([149], range(50, 100)), (1, 0),  # Edge between 4 and 6
             (range(150, 200), [49]), (0, 1))
    )
    for instruction in instructions:
        try:
            position, direction = walk_cube(board, edges, position, direction, int(instruction))
        except ValueError:
            direction = rotate(direction, instruction)
    print(get_password(position, direction))



if __name__ == "__main__":
    main()
