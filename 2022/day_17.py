def collides(chamber, rock_shape, rock_position):
    if rock_position[0] < 0 or rock_position[0] + len(rock_shape[0]) > 7:
        return True

    for rock_y in range(len(rock_shape)-1, -1, -1):
        chamber_y = rock_position[1] - rock_y
        for rock_x, is_rock in enumerate(rock_shape[rock_y]):
            chamber_x = rock_position[0] + rock_x
            if chamber_y < len(chamber) and chamber[chamber_y][chamber_x] and rock_shape[rock_y][rock_x]:
                return True
    return False


def update_chamber(chamber, rock_shape, rock_position):
    for rock_y in range(len(rock_shape)-1, -1, -1):
        chamber_y = rock_position[1] - rock_y
        for rock_x, is_rock in enumerate(rock_shape[rock_y]):
            chamber_x = rock_position[0] + rock_x
            if not chamber_y < len(chamber):
                chamber.append([0] * 7)
            if rock_shape[rock_y][rock_x]:
                chamber[chamber_y][chamber_x] = rock_shape[rock_y][rock_x]


def check_for_pattern(rock_history):
    pattern_start = rock_history[-1]
    pattern = [pattern_start]
    for i in range(len(rock_history)-2, len(rock_history) // 2 - 1, -1):
        if rock_history[i] == pattern_start:
            if list(reversed(pattern)) == rock_history[i-len(pattern)+1:i+1]:
                return pattern
        else:
            pattern.append(rock_history[i])


def get_tower_height(rock_amount, rock_shapes, jet_patterns):
    chamber = [[1] * 7]

    jet_passes = 0
    is_recording_pattern = False
    start_of_pattern_height = None
    start_of_pattern_rock = None
    start_of_pattern_jet = None
    pattern_length = 0
    height_skipped = 0

    rock_shape_counter = 0
    jet_pattern_counter = 0
    rock_counter = 0
    while rock_counter < rock_amount:
        rock_counter += 1
        if jet_passes > 1 and not height_skipped:  # Wait for the rocks to hit a steady, repeating pattern
            if not is_recording_pattern:
                start_of_pattern_height = len(chamber)
                is_recording_pattern = True
                start_of_pattern_rock = rock_shape_counter  # Store what rock the pattern starts with
                start_of_pattern_jet = jet_pattern_counter  # Store what jet the pattern starts with
            elif rock_shape_counter == start_of_pattern_rock and jet_pattern_counter == start_of_pattern_jet:
                # When the current rock and jet counts are the same as the start of the pattern, it means the pattern has completed
                pattern_height = len(chamber) - start_of_pattern_height
                rocks_to_go = rock_amount - rock_counter
                patterns_skipped = rocks_to_go // pattern_length
                rock_counter += patterns_skipped * pattern_length
                height_skipped = patterns_skipped * pattern_height
                is_recording_pattern = False

        rock_shape = rock_shapes[rock_shape_counter]
        rock_shape_counter = (rock_shape_counter+1) % len(rock_shapes)
        rock_position = (2, len(rock_shape) + len(chamber) + 2)

        while True:
            jet_direction = jet_patterns[jet_pattern_counter]
            jet_pattern_counter = (jet_pattern_counter+1) % len(jet_patterns)
            if jet_pattern_counter == 0:
                jet_passes += 1

            new_rock_position = (rock_position[0] + (1 if jet_direction == ">" else -1), rock_position[1])
            if not collides(chamber, rock_shape, new_rock_position):
                rock_position = new_rock_position

            new_rock_position = (rock_position[0], rock_position[1]-1)
            if not collides(chamber, rock_shape, new_rock_position):
                rock_position = new_rock_position
            else:
                if is_recording_pattern:
                    pattern_length += 1
                update_chamber(chamber, rock_shape, rock_position)
                break

    # for row in reversed(chamber[1:]):
    #     print("|", *("#" if elem else "." for elem in row), "|", sep="")
    #
    # print("+-------+")

    return len(chamber)-1 + height_skipped


def main():
    with open("day_17_input", "r") as f:
        jet_patterns = f.read()

    rock_shapes = (
        ((1, 1, 1, 1),),

        ((0, 1, 0),
         (1, 1, 1),
         (0, 1, 0)),

        ((0, 0, 1),
         (0, 0, 1),
         (1, 1, 1)),

        ((1,),
         (1,),
         (1,),
         (1,)),

        ((1, 1),
         (1, 1))
    )

    print(get_tower_height(2022, rock_shapes, jet_patterns))
    print()
    print(get_tower_height(1000000000000, rock_shapes, jet_patterns))


if __name__ == '__main__':
    main()
