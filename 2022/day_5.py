from itertools import zip_longest
from copy import deepcopy

stacks = []
instructions = []


with open("day_5_input", "r") as f:
    crates_per_level = []
    while "[" in (line := next(f)[:-1]):
        crates_per_level.append([line[i] for i in range(1, len(line), 4)])

    for stack in zip_longest(*reversed(crates_per_level), fillvalue=" "):
        stacks.append([crate for crate in stack if crate != " "])

    next(f)  # Skip over the empty line

    for line in (x.strip() for x in f):
        words = line.split()
        instructions.append([int(words[i]) for i in range(1, len(words), 2)])

stacks_copy = deepcopy(stacks)

for amount, source, destination in instructions:
    source -= 1
    destination -= 1
    crates_to_move = stacks_copy[source][-amount:]
    del stacks_copy[source][-amount:]
    stacks_copy[destination].extend(reversed(crates_to_move))

print(*(stack[-1] for stack in stacks_copy), sep="")


for amount, source, destination in instructions:
    source -= 1
    destination -= 1
    crates_to_move = stacks[source][-amount:]
    del stacks[source][-amount:]
    stacks[destination].extend(crates_to_move)

print()
print(*(stack[-1] for stack in stacks), sep="")
