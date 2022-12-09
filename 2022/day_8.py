import functools
import operator


trees = []

with open("day_8_input", "r") as f:
    for row in (x.strip() for x in f):
        trees.append(list(map(int, row)))


visible_trees = set()
for line_iters in ((((x, y) for y in range(len(trees[0]))) for x in range(len(trees))),             # Go through each row from left to right
                   (((x, y) for y in range(len(trees[0])-1, -1, -1)) for x in range(len(trees))),   # Go through each row from right to left
                   (((x, y) for x in range(len(trees))) for y in range(len(trees[0]))),             # Go through each column from top to bottom
                   (((x, y) for x in range(len(trees)-1, -1, -1)) for y in range(len(trees[0])))):  # Go through each row from bottom to top
    for line_iter in line_iters:
        visibility = -1
        for x, y in line_iter:
            tree = trees[x][y]
            if trees[x][y] > visibility:
                visibility = trees[x][y]
                visible_trees.add((x, y))
                if visibility == 9:
                    break

print(len(visible_trees))


max_score = 0
for x in range(1, len(trees)-1):
    for y in range(1, len(trees[0])-1):
        treehouse = trees[x][y]
        distances = []
        for line_iter in (((x_check, y) for x_check in range(x+1, len(trees))),
                          ((x_check, y) for x_check in range(x-1, -1, -1)),
                          ((x, y_check) for y_check in range(y + 1, len(trees[0]))),
                          ((x, y_check) for y_check in range(y - 1, -1, -1))):
            distance = 0
            for x_view, y_view in line_iter:
                distance += 1
                if trees[x_view][y_view] >= treehouse:
                    break
            distances.append(distance)
        score = functools.reduce(operator.mul, distances)
        if score > max_score:
            max_score = score

print()
print(max_score)
