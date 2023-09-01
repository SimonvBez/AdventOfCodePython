elfs = []

with open("day_1_input", "r") as f:
    elf = 0
    for line in (x.strip() for x in f):
        if line:
            elf += int(line)
        else:
            elfs.append(elf)
            elf = 0

print(max(elfs))

calories_per_elf_sorted = sorted(elfs)
top_3_calories = calories_per_elf_sorted[-3:]
print()
print(sum(top_3_calories))
