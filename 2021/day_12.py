def is_small_cave(cave):
    return cave.islower()


def remove_cave(board, cave):
    result = board.copy()
    del result[cave]
    return result


def find_paths(board, current_cave, destination, double_small_cave=None, double_count=0):
    if current_cave == destination:
        return double_small_cave is None or double_count == 2

    next_caves = board[current_cave]
    if is_small_cave(current_cave):
        if current_cave != double_small_cave or double_count:
            board = remove_cave(board, current_cave)
        double_count += current_cave == double_small_cave
    route_sum = 0
    for next_cave in next_caves:
        if next_cave in board:
            route_sum += find_paths(board, next_cave, destination, double_small_cave, double_count)
    return route_sum


def main():
    board = {}
    with open("day_12_input") as f:
        for line in (x.rstrip() for x in f):
            cave_a, cave_b = line.split("-")
            if cave_a not in board:
                board[cave_a] = set()
            if cave_b not in board:
                board[cave_b] = set()
            board[cave_a].add(cave_b)
            board[cave_b].add(cave_a)

    no_doubles_paths = find_paths(board, "start", "end")
    print(no_doubles_paths)

    small_caves = (cave for cave in board if is_small_cave(cave) and cave not in ("start", "end"))
    print(sum(find_paths(board, "start", "end", double_small_cave) for double_small_cave in small_caves) + no_doubles_paths)


if __name__ == "__main__":
    main()
