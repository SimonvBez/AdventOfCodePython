moves = []

with open("day_2_input", "r") as f:
    for line in (x.strip() for x in f):
        moves.append(line.split(" "))

sum_points = 0
for opponent, mine in moves:
    opponent = ord(opponent) - ord("A")
    mine = ord(mine) - ord("X") + 1

    sum_points += mine
    sum_points += 3 * ((mine - opponent) % 3)

print(sum_points)


sum_points = 0
for opponent, outcome in moves:
    opponent = ord(opponent) - ord("A")
    outcome = ord(outcome) - ord("X")

    sum_points += outcome * 3
    sum_points += (opponent + outcome + 2) % 3 + 1

print()
print(sum_points)
