from functools import reduce
from operator import mul


def adjacent_iter(x, y, len_x, len_y):
    if x-1 >= 0:
        yield x-1, y
    if x+1 < len_x:
        yield x+1, y
    if y - 1 >= 0:
        yield x, y-1
    if y + 1 < len_y:
        yield x, y+1


def main():
    heightmap = []

    with open("day_9_input", "r") as f:
        for row in (x.strip() for x in f):
            heightmap.append(list(map(int, row)))

    low_points = []
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            tile = heightmap[x][y]
            if all(heightmap[adj_x][adj_y] > tile for adj_x, adj_y in adjacent_iter(x, y, len(heightmap), len(heightmap[0]))):
                low_points.append((x, y))

    print(sum(heightmap[x][y] + 1 for x, y in low_points))

    basins = []
    for low_point in low_points:
        tiles_to_check = [low_point]
        basin = []
        while tiles_to_check:
            coord = tiles_to_check.pop(0)
            tile_x, tile_y = coord
            tile_height = heightmap[tile_x][tile_y]
            if tile_height < 9 and coord not in basin:
                basin.append(coord)
                tiles_to_check.extend(adjacent_iter(tile_x, tile_y, len(heightmap), len(heightmap[0])))

        basins.append(basin)

    basins.sort(key=lambda b: -len(b))
    print()
    print(reduce(mul, (len(b) for b in basins[:3])))


if __name__ == "__main__":
    main()
