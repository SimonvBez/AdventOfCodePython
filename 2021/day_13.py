def fold(dots, split):
    axis, fold_coord = split
    if axis == "x":
        dim = 0
    else:
        dim = 1

    folded_dots = []
    for dot in dots:
        if dot[dim] > fold_coord:
            folded_dots.append(dot)

    for dot in folded_dots:
        dots.remove(dot)
        if dim == 0:
            folded_dot = (fold_coord - (dot[0] - fold_coord), dot[1])
        else:
            folded_dot = (dot[0], fold_coord - (dot[1] - fold_coord))
        dots.add(folded_dot)


def print_paper(dots):
    max_x, max_y = map(max, zip(*dots))
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in dots:
                print("##", end="")
            else:
                print("  ", end="")
        print()


def main():
    dots = set()
    splits = []
    with open("day_13_input") as f:
        for line in (x.rstrip() for x in f):
            if not line:
                break
            dots.add(tuple(map(int, line.split(","))))

        for line in (x.rstrip() for x in f):
            axis, coord = line[11:].split("=")
            splits.append((axis, int(coord)))

    splits_iter = iter(splits)
    fold(dots, next(splits_iter))
    print(len(dots))

    for split in splits_iter:
        fold(dots, split)
    print_paper(dots)


if __name__ == "__main__":
    main()
