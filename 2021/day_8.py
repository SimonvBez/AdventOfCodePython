entries = []

with open("day_8_input", "r") as f:
    for line in (x.strip() for x in f):
        signal_patterns, output_values = line.split(" | ")
        entries.append([list(map(set, signal_patterns.split(" "))), output_values.split(" ")])

appearance_1478_count = 0
for signal_patterns, output_values in entries:
    for output_value in output_values:
        if len(output_value) in (2, 3, 4, 7):
            appearance_1478_count += 1

print(appearance_1478_count)


digits = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
digit_sets = list(map(set, digits))
value_sum = 0
for signal_patterns, output_values in entries:
    translation = {}
    wires_1 = set(next(wires for wires in digit_sets if len(wires) == 2))
    for wires in signal_patterns:
        match len(wires):
            case 2:
                wires_1 = wires
            case 3:
                wires_7 = wires
            case 4:
                wires_4 = wires
            case 7:
                wires_8 = wires

    for wires in signal_patterns:
        if len(wires) == 6:
            if len(wires & wires_1) == 1:
                wires_6 = wires
        if len(wires) == 5:
            if len(wires & wires_1) == 2:
                wires_3 = wires

    translation[(wires_7 - wires_1).pop()] = "a"
    translation[(wires_4 - wires_3).pop()] = "b"
    translation[(wires_1 - wires_6).pop()] = "c"
    translation[((wires_4 - wires_1) & wires_3).pop()] = "d"
    translation[(wires_8 - wires_3 - wires_4).pop()] = "e"
    translation[(wires_1 & wires_6).pop()] = "f"
    translation[(wires_8 - set(translation.keys())).pop()] = "g"

    translation = {ord(c1): ord(c2) for c1, c2 in translation.items()}

    true_output_value_sets = [set(values.translate(translation)) for values in output_values]
    true_output_value = int("".join(map(str, [digit_sets.index(s) for s in true_output_value_sets])))
    value_sum += true_output_value

print()
print(value_sum)
