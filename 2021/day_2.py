pos_horizontal = 0
depth = 0

instructions = []

with open("day_2_input", "r") as f:
    for line in (x.strip() for x in f):
        command, value = line.split(" ")
        instructions.append((command, int(value)))


for command, value in instructions:
    match command:
        case "forward":
            pos_horizontal += value
        case "up":
            depth -= value
        case "down":
            depth += value

print(f"Horizontal position: {pos_horizontal}")
print(f"Depth: {depth}")
print(f"Product: {pos_horizontal * depth}")


pos_horizontal = 0
depth = 0
aim = 0

for command, value in instructions:
    match command:
        case "forward":
            pos_horizontal += value
            depth += aim * value
        case "up":
            aim -= value
        case "down":
            aim += value

print("\n")
print(f"Horizontal position: {pos_horizontal}")
print(f"Depth: {depth}")
print(f"Product: {pos_horizontal * depth}")
