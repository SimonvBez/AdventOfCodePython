from functools import reduce


def grouped(iterable, n):
    """s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."""
    return zip(*[iter(iterable)]*n)


def get_item_priority(character):
    ascii_val = ord(character)
    if 65 <= ascii_val <= 90:
        return ascii_val - 38
    else:
        return ascii_val - 96


rucksacks = []

with open("day_3_input", "r") as f:
    for line in (x.strip() for x in f):
        rucksacks.append(line)

priority_sum = 0
for items in rucksacks:
    half_i = len(items) // 2
    compartment1, compartment2 = items[:half_i], items[half_i:]
    common_item = (set(compartment1) & set(compartment2)).pop()
    priority_sum += get_item_priority(common_item)

print(priority_sum)


priority_sum = 0
for group in grouped(rucksacks, 3):
    sets = map(set, group)
    common_element = reduce(lambda a, b: a & b, sets).pop()
    priority_sum += get_item_priority(common_element)

print()
print(priority_sum)
