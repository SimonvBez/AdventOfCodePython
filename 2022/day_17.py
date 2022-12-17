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
            chamber[chamber_y][chamber_x] = rock_shape[rock_y][rock_x]


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
    jet_pattern_counter = 0
    rock_shape_counter = 0
    chamber = [[1] * 7]

    for _ in range(2022):
        rock_shape = rock_shapes[rock_shape_counter]
        rock_shape_counter = (rock_shape_counter+1) % len(rock_shapes)
        rock_position = (2, len(rock_shape) + len(chamber) + 2)

        while True:
            jet_direction = jet_patterns[jet_pattern_counter]
            jet_pattern_counter = (jet_pattern_counter+1) % len(jet_patterns)

            if jet_direction == "<":
                new_rock_position = (rock_position[0]-1, rock_position[1])
                if not collides(chamber, rock_shape, new_rock_position):
                    rock_position = new_rock_position
            else:
                new_rock_position = (rock_position[0]+1, rock_position[1])
                if not collides(chamber, rock_shape, new_rock_position):
                    rock_position = new_rock_position

            new_rock_position = (rock_position[0], rock_position[1]-1)
            if not collides(chamber, rock_shape, new_rock_position):
                rock_position = new_rock_position
            else:
                update_chamber(chamber, rock_shape, rock_position)
                break

    # for row in reversed(chamber[1:]):
    #     print(*("#" if elem else "." for elem in row), sep="")

    print(len(chamber)-1)


if __name__ == '__main__':
    main()
