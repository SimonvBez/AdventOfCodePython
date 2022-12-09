def is_adjacent(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])) <= 1


def get_tail_history(movements, tail_length):
    pos_head = (0, 0)
    pos_tails = [(0, 0)] * tail_length
    tail_history = [pos_tails[-1]]

    for direction, amount in movements:
        for _ in range(amount):
            head_x, head_y = pos_head
            match direction:
                case "R":
                    pos_head = (head_x+1, head_y)
                case "L":
                    pos_head = (head_x-1, head_y)
                case "U":
                    pos_head = (head_x, head_y+1)
                case "D":
                    pos_head = (head_x, head_y-1)
            for i in range(len(pos_tails)):
                pos_knot = pos_tails[i]
                pos_next_knot = pos_tails[i-1] if i else pos_head
                if not is_adjacent(pos_knot, pos_next_knot):
                    movement_x = min(max(pos_next_knot[0] - pos_knot[0], -1), 1)
                    movement_y = min(max(pos_next_knot[1] - pos_knot[1], -1), 1)
                    new_pos = (pos_knot[0] + movement_x, pos_knot[1] + movement_y)
                    pos_tails[i] = new_pos
                    if i == len(pos_tails)-1:
                        tail_history.append(new_pos)
    return set(tail_history)


def main():
    movements = []
    with open("day_9_input", "r") as f:
        for line in (x.strip() for x in f):
            direction, amount = line.split()
            movements.append((direction, int(amount)))

    print(len(get_tail_history(movements, 1)))
    print()
    print(len(get_tail_history(movements, 9)))


if __name__ == "__main__":
    main()
