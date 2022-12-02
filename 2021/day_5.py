def main():
    lines = []
    with open("day_5_input", "r") as f:
        for line in (x.strip() for x in f):
            point1, point2 = line.split(" -> ")
            point1 = [int(num) for num in point1.split(",")]
            point2 = [int(num) for num in point2.split(",")]
            lines.append((point1, point2))

    field = []
    for _ in range(1000):
        field.append([0] * 1000)

    for point1, point2 in lines:
        if point1[0] == point2[0]:
            for y in range(min(point1[1], point2[1]), max(point1[1], point2[1])+1):
                field[point1[0]][y] += 1
        elif point1[1] == point2[1]:
            for x in range(min(point1[0], point2[0]), max(point1[0], point2[0])+1):
                field[x][point1[1]] += 1
        elif abs(point1[0] - point2[0]) == abs(point1[1] - point2[1]):
            x, y = point1
            x_end, y_end = point2
            x_step = 1 if x <= x_end else -1
            y_step = 1 if y <= y_end else -1
            x_end += x_step
            while x != x_end:
                field[x][y] += 1
                x += x_step
                y += y_step

    total_overlaps = 0
    for row in field:
        for num in row:
            total_overlaps += num >= 2
    print(total_overlaps)


if __name__ == "__main__":
    main()
