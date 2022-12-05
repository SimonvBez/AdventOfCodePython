elfs = []

with open("day_1_input", "r") as f:
    elf = []
    for line in (x.strip() for x in f):
        if line:
            elf.append(int(line))
        else:
            elfs.append(elf)
            elf = []

calories_per_elf = [sum(calories) for calories in elfs]
top_calories = max(calories_per_elf)
print(f"Amount of calories the Elf with the most calories has: {top_calories}")

calories_per_elf_sorted = sorted(calories_per_elf, key=lambda x: -x)
top_3_calories = calories_per_elf_sorted[:3]
top_3_calories_sum = sum(top_3_calories)
print(f"Amount of calories the top 3 Elfs with the most calories have combined: {top_3_calories_sum}")
