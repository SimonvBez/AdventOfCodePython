from functools import reduce


def count_sides_facing_num(array_3d, lava_val, num):
    exposed_counter = 0
    for x in range(1, len(array_3d)-1):
        for y in range(1, len(array_3d)-1):
            for z in range(1, len(array_3d)-1):
                if array_3d[x][y][z] == lava_val:
                    for adj_coords in adjacent_iterator(x, y, z):
                        if subscript_array(array_3d, adj_coords) == num:
                            exposed_counter += 1

    return exposed_counter


def adjacent_iterator(*coords):
    for i in range(len(coords)):
        yield *coords[:i], coords[i]+1, *coords[i+1:]
        yield *coords[:i], coords[i]-1, *coords[i+1:]


def subscript_array(array, coords):
    return reduce(lambda arr, subscript: arr[subscript], coords, array)


def main():
    all_cubes = []
    with open("day_18_input", "r") as f:
        for line in (x.strip() for x in f):
            all_cubes.append(tuple(map(int, line.split(","))))

    max_coord = 0
    for cube in all_cubes:
        for i, coord in enumerate(cube):
            if coord > max_coord:
                max_coord = coord

    droplet_3d = [[[0] * (max_coord+3) for _ in range(max_coord+3)] for _ in range(max_coord+3)]
    for x, y, z in all_cubes:
        droplet_3d[x+1][y+1][z+1] = 1

    print(count_sides_facing_num(droplet_3d, 1, 0))

    air_outside_queue = [(0, 0, 0)]
    while air_outside_queue:
        x, y, z = air_outside_queue.pop()
        droplet_3d[x][y][z] = 2
        for adj_coords in adjacent_iterator(x, y, z):
            if 0 <= min(adj_coords) and max(adj_coords) < len(droplet_3d):
                if subscript_array(droplet_3d, adj_coords) == 0:
                    air_outside_queue.append(adj_coords)

    print()
    print(count_sides_facing_num(droplet_3d, 1, 2))


if __name__ == "__main__":
    main()
