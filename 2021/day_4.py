boards: list[list[list[int | float]]] = []


def update_board(board: list[list[int | float]], drawn_number):
    board_updated = False
    for row in board:
        for i, number in enumerate(row):
            if number == drawn_number:
                row[i] = float(number)
                board_updated = True
    if board_updated:
        for row in board:
            if all(isinstance(num, float) for num in row):
                return True
        for column in zip(*board):
            if all(isinstance(num, float) for num in column):
                return True
    return False


def main():
    with open("day_4_input", "r") as f:
        drawn_numbers = [int(num) for num in next(f).split(",")]

        board = []
        for line in (x.strip() for x in f):
            if line:
                board.append([int(num) for num in line.split()])
            else:
                if board:
                    boards.append(board)
                board = []

    won_boards = []
    while boards:
        for drawn_number in drawn_numbers:
            won_board_indexes = []
            for i, board in enumerate(boards):
                if update_board(board, drawn_number):
                    won_board_indexes.append(i)
                    won_boards.append([board, drawn_number])
            for i in reversed(won_board_indexes):
                del boards[i]

    for won_board in won_boards:
        board = won_board[0]
        sum_unmarked_numbers = 0
        for row in board:
            for num in (num for num in row if isinstance(num, int)):
                sum_unmarked_numbers += num
        won_board.append(sum_unmarked_numbers)
    print(won_boards[0][1] * won_boards[0][2])
    print(won_boards[-1][1] * won_boards[-1][2])


if __name__ == "__main__":
    main()
