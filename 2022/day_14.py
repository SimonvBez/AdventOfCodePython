from itertools import pairwise
import copy


def sand_fall_iter(x, y):
    yield x, y+1
    yield x-1, y+1
    yield x+1, y+1


def main():
    tile_columns: dict[int, set] = {}
    with open("day_14_input", "r") as f:
        for line in (x.strip() for x in f):
            coord_strings = line.split(" -> ")
            path_coords = [tuple(map(int, coord.split(","))) for coord in coord_strings]
            for coord_start, coord_end in pairwise(path_coords):
                if coord_start[0] == coord_end[0]:
                    x = coord_start[0]
                    y_start = min(coord_start[1], coord_end[1])
                    y_end = max(coord_start[1], coord_end[1]) + 1
                    if x not in tile_columns:
                        tile_columns[x] = set()
                    for y in range(y_start, y_end):
                        tile_columns[x].add(y)
                else:
                    y = coord_start[1]
                    x_start = min(coord_start[0], coord_end[0])
                    x_end = max(coord_start[0], coord_end[0]) + 1
                    for x in range(x_start, x_end):
                        if x not in tile_columns:
                            tile_columns[x] = {y}
                        else:
                            tile_columns[x].add(y)

    tile_columns_original = copy.deepcopy(tile_columns)

    rest_counter = 0
    is_dropping_sand = True
    sand_start_point = (500, 0)
    cur_x, cur_y = sand_start_point
    previous_point = []
    while is_dropping_sand:
        for new_x, new_y in sand_fall_iter(cur_x, cur_y):  # Check if the sand can fall
            if new_x not in tile_columns:
                # Sand is falling in a column with no rocks
                is_dropping_sand = False
                break
            if new_y not in tile_columns[new_x]:  # Check if this new coord is free
                if cur_y > max(tile_columns[new_x]):
                    is_dropping_sand = False
                    break
                previous_point.append((cur_x, cur_y))
                cur_x, cur_y = new_x, new_y  # Move the sand to the new coord
                break
        else:
            # The sand could not fall down; let it come to rest
            rest_counter += 1
            tile_columns[cur_x].add(cur_y)
            if previous_point:
                cur_x, cur_y = previous_point.pop()
            else:
                is_dropping_sand = False

    print(rest_counter)

    tile_columns = tile_columns_original
    floor_y = max(max(column) for column in tile_columns.values()) + 2

    rest_counter = 0
    is_dropping_sand = True
    sand_start_point = (500, 0)
    cur_x, cur_y = sand_start_point
    previous_point = []
    while is_dropping_sand:
        for new_x, new_y in sand_fall_iter(cur_x, cur_y):  # Check if the sand can fall
            if new_x not in tile_columns:
                # Sand is falling in a column with no rocks
                tile_columns[new_x] = set()
            if new_y not in tile_columns[new_x] and new_y < floor_y:  # Check if this new coord is free
                previous_point.append((cur_x, cur_y))
                cur_x, cur_y = new_x, new_y  # Move the sand to the new coord
                break
        else:
            # The sand could not fall down; let it come to rest
            rest_counter += 1
            tile_columns[cur_x].add(cur_y)
            if previous_point:
                cur_x, cur_y = previous_point.pop()
            else:
                is_dropping_sand = False

    print()
    print(rest_counter)


if __name__ == '__main__':
    main()
