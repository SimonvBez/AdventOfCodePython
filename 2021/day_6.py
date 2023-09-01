with open("day_6_input", "r") as f:
    fish = [int(num) for num in f.read().split(",")]


fishes_per_day = [0] * 9
for days_left in fish:
    fishes_per_day[days_left] += 1

for _ in range(256):
    fishes_per_day.append(fishes_per_day.pop(0))
    fishes_per_day[6] += fishes_per_day[8]

print(sum(fishes_per_day))
