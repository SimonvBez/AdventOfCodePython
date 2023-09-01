class Valley:
    def __init__(self, valley_height, valley_width, blizzards_up, blizzards_down, blizzards_left, blizzards_right):
        self.valley_height = valley_height
        self.valley_width = valley_width
        self.blizzards_up = blizzards_up
        self.blizzards_down = blizzards_down
        self.blizzards_left = blizzards_left
        self.blizzards_right = blizzards_right

    def is_clear(self, y, x, time_passed):
        return not (0 <= y < self.valley_height and 0 <= x < self.valley_width) \
           or (y + time_passed) % self.valley_height not in self.blizzards_up[x] \
           and (y - time_passed) % self.valley_height not in self.blizzards_down[x] \
           and (x + time_passed) % self.valley_width not in self.blizzards_left[y] \
           and (x - time_passed) % self.valley_width not in self.blizzards_right[y]

    def steps_iter(self, position):
        y, x = position
        if y + 1 < self.valley_height:
            yield y + 1, x
        if y - 1 >= 0:
            yield y - 1, x
        if x + 1 < self.valley_width and y >= 0:
            yield y, x + 1
        if x - 1 >= 0 and y < self.valley_height:
            yield y, x - 1
        yield y, x

    def find_exit(self, start_position, end_position, time_passed=0):
        possible_positions = {start_position}
        while True:
            new_positions = set()
            time_passed += 1
            for current_position in possible_positions:
                if current_position == end_position:
                    return time_passed

                for next_position in self.steps_iter(current_position):
                    if not self.is_clear(*next_position, time_passed):
                        continue
                    new_positions.add(next_position)

            possible_positions = new_positions


def main():
    with open("day_24_input", "r") as f:
        lines = tuple(x.rstrip() for x in f)

    valley_height = len(lines) - 2
    valley_width = len(lines[0]) - 2
    blizzards_up = tuple(set() for _ in range(valley_width))
    blizzards_down = tuple(set() for _ in range(valley_width))
    blizzards_left = tuple(set() for _ in range(valley_height))
    blizzards_right = tuple(set() for _ in range(valley_height))

    for y, line in enumerate(lines[1:-1]):
        for x, char in enumerate(line[1:-1]):
            if char == ">":
                blizzards_right[y].add(x)
            elif char == "<":
                blizzards_left[y].add(x)
            elif char == "v":
                blizzards_down[x].add(y)
            elif char == "^":
                blizzards_up[x].add(y)

    valley = Valley(valley_height, valley_width, blizzards_up, blizzards_down, blizzards_left, blizzards_right)
    passed_time = valley.find_exit((-1, 0), (valley_height-1, valley_width-1))
    print(passed_time)

    passed_time = valley.find_exit((valley_height, valley_width-1), (0, 0), passed_time)
    print(valley.find_exit((-1, 0), (valley_height-1, valley_width-1), passed_time))


if __name__ == "__main__":
    main()
