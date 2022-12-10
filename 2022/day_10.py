instructions = []
with open("day_10_input", "r") as f:
    for line in (x.strip() for x in f):
        instruction = line.split()
        if len(instruction) == 2:
            instruction[1] = int(instruction[1])
        instructions.append(instruction)

cycles_to_check = [20] + list(range(60, 221, 40))
cycles_completed = 0
x_value = 1

x_sum = 0

for instruction in instructions:
    inst_code = instruction[0]
    previous_x = x_value
    if inst_code == "addx":
        x_value += instruction[1]
        cycles_completed += 2
    elif inst_code == "noop":
        cycles_completed += 1

    if cycles_to_check and cycles_completed >= cycles_to_check[0]:
        x_sum += previous_x * cycles_to_check.pop(0)

print(x_sum)


crt_screen = [[" " for _ in range(40)] for _ in range(6)]
current_instruction = None
cycles_left = 0
x_value = 1
for cycle in range(1, 241):
    # Begin of cycle
    if not cycles_left:
        current_instruction = instructions.pop(0)
        if current_instruction[0] == "addx":
            cycles_left = 2
        elif current_instruction[0] == "noop":
            cycles_left = 1

    # During cycle
    pixel_y, pixel_x = divmod(cycle-1, 40)
    if abs(pixel_x - x_value) <= 1:
        crt_screen[pixel_y][pixel_x] = "█"

    # After cycle
    cycles_left -= 1
    if not cycles_left:
        if current_instruction[0] == "addx":
            x_value += current_instruction[1]


print()
print(*("".join(row) for row in crt_screen), sep="\n")
