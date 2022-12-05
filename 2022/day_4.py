pairs = []

with open("day_4_input", "r") as f:
    for line in (x.strip() for x in f):
        elf_strings = line.split(",")
        sections = []
        for elf_string in elf_strings:
            sections.append(list(map(int, elf_string.split("-"))))
        pairs.append(sections)

fully_contains_range_count = 0
for elf1, elf2 in pairs:
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or \
            (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        fully_contains_range_count += 1

print(fully_contains_range_count)


has_overlap_count = 0
for elf1, elf2 in pairs:
    if max(elf1[0], elf2[0]) <= min(elf1[1], elf2[1]):
        has_overlap_count += 1

print()
print(has_overlap_count)