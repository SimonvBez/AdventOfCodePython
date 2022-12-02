moves = []

with open("day_2_input", "r") as f:
    for line in (x.strip() for x in f):
        moves.append(line.split(" "))

sum_points = 0
for opponent, mine in moves:
    match mine:
        case "X":
            sum_points += 1
            round_points = {"A": 3, "B": 0, "C": 6}
        case "Y":
            sum_points += 2
            round_points = {"A": 6, "B": 3, "C": 0}
        case "Z":
            sum_points += 3
            round_points = {"A": 0, "B": 6, "C": 3}
    sum_points += round_points[opponent]

print(sum_points)


sum_points = 0
for opponent, outcome in moves:
    match outcome:
        case "X":
            sum_points += 0
            my_moves = {"A": 3, "B": 1, "C": 2}
        case "Y":
            sum_points += 3
            my_moves = {"A": 1, "B": 2, "C": 3}
        case "Z":
            sum_points += 6
            my_moves = {"A": 2, "B": 3, "C": 1}

    sum_points += my_moves[opponent]

print()
print(sum_points)
