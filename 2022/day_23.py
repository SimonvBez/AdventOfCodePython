from copy import deepcopy


class Position:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return hash((self.y, self.x))

    def __repr__(self):
        return f"Pos({self.y}, {self.x})"


class Elf:
    def __init__(self, pos_y, pos_x):
        self.position = Position(pos_y, pos_x)
        self.proposition = None

    def __repr__(self):
        return f"Elf({self.position})"


def get_rect_size(elves: list[Elf]):
    top = left = 10000
    bottom = right = -10000
    for elf in elves:
        if elf.position.y < top:
            top = elf.position.y
        if elf.position.y > bottom:
            bottom = elf.position.y
        if elf.position.x < left:
            left = elf.position.x
        if elf.position.x > right:
            right = elf.position.x
    return bottom - top + 1, right - left + 1


def look_iter(pos: Position, direction: tuple[int, int]):
    if direction[0]:
        for i in range(-1, 2):
            yield Position(pos.y + direction[0], pos.x + i)
    else:
        for i in range(-1, 2):
            yield Position(pos.y + i, pos.x + direction[1])


def adjacent_iter(pos: Position):
    for i in range(-1, 2):
        yield Position(pos.y + 1, pos.x + i)
        yield Position(pos.y - 1, pos.x + i)
    yield Position(pos.y, pos.x + 1)
    yield Position(pos.y, pos.x - 1)


def direction_iter(directions, start):
    length = len(directions)
    for i in range(length):
        yield directions[(i + start) % length]


def simulate_round(elves: list[Elf], look_directions, current_direction):
    has_moved = False
    elf_positions = set(elf.position for elf in elves)
    propositions: dict[Position, Elf] = {}
    for elf in elves:
        if not any(adj_pos in elf_positions for adj_pos in adjacent_iter(elf.position)):
            continue

        for direction in direction_iter(look_directions, current_direction):
            if any(look_pos in elf_positions for look_pos in look_iter(elf.position, direction)):
                continue
            # This elf can propose in this direction
            proposition = Position(elf.position.y + direction[0], elf.position.x + direction[1])
            if proposition in propositions:
                # The proposed tile already has a proposition on it. Tell the other elf not to move
                propositions[proposition].proposition = None
            else:
                # The proposed tile is unclaimed. Add it to the dict and the elf
                propositions[proposition] = elf
                elf.proposition = proposition
            break

    for elf in elves:
        if elf.proposition:
            has_moved = True
            elf.position = elf.proposition
            elf.proposition = None

    return has_moved


def main():
    elves = []
    with open("day_23_input", "r") as f:
        for y, line in enumerate((x.rstrip() for x in f)):
            for x, char in enumerate(line):
                if char == "#":
                    elves.append(Elf(y, x))
    elves_input = deepcopy(elves)

    look_directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    current_direction = 0

    for _ in range(10):
        simulate_round(elves, look_directions, current_direction)
        current_direction += 1
        current_direction %= 4
    rect_height, rect_width = get_rect_size(elves)
    print(rect_height * rect_width - len(elves))

    elves = elves_input
    round_counter = 1
    current_direction = 0
    while simulate_round(elves, look_directions, current_direction):
        current_direction += 1
        current_direction %= 4
        round_counter += 1

    print(round_counter)


if __name__ == "__main__":
    main()
