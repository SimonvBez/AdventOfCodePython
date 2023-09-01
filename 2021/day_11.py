import itertools
import copy


def adjacent_iter(y, x, board_height, board_width):
    x_too_low = x == 0
    x_too_high = x == board_width - 1
    if y > 0:
        if not x_too_low:
            yield y-1, x-1
        yield y-1, x
        if not x_too_high:
            yield y-1, x+1

    if not x_too_low:
        yield y, x-1
    if not x_too_high:
        yield y, x+1

    if y < board_height - 1:
        if not x_too_low:
            yield y+1, x-1
        yield y+1, x
        if not x_too_high:
            yield y+1, x+1


def check_flash(board, y, x):
    if board[y][x] == 10:
        for adj_y, adj_x in adjacent_iter(y, x, len(board), len(board[0])):
            board[adj_y][adj_x] += 1
            check_flash(board, adj_y, adj_x)


def do_step(board):
    flash_counter = 0
    for y, row in enumerate(board):
        for x in range(len(row)):
            row[x] += 1
            check_flash(board, y, x)

    for row in board:
        for x, octopus in enumerate(row):
            if octopus >= 10:
                flash_counter += 1
                row[x] = 0
    return flash_counter


def get_first_all_flash(board):
    octopus_count = len(board) * len(board[0])
    for step in itertools.count(1):
        if do_step(board) == octopus_count:
            return step


def count_flashes(board, steps):
    flash_counter = 0
    for _ in range(steps):
        flash_counter += do_step(board)

    return flash_counter


def main():
    board = []
    with open("day_11_input") as f:
        for line in (x.rstrip() for x in f):
            board.append(list(map(int, line)))

    print(count_flashes(copy.deepcopy(board), 100))
    print(get_first_all_flash(board))


if __name__ == "__main__":
    main()
