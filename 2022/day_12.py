import time
import ctypes


def adjacent_iter(x, y, len_x, len_y):
    if x-1 >= 0:
        yield x-1, y
    if x+1 < len_x:
        yield x+1, y
    if y-1 >= 0:
        yield x, y-1
    if y+1 < len_y:
        yield x, y+1


def count_steps(heightmap, start_pos, step_condition, result_condition):
    mapped_coordinates = {start_pos}
    current_map_queue = [start_pos]
    step_count = 1

    while current_map_queue:
        next_map_queue = []
        for tile_coord in current_map_queue:
            tile_x, tile_y = tile_coord
            tile_height = heightmap[tile_x][tile_y]
            for adj_coord in adjacent_iter(tile_x, tile_y, len(heightmap), len(heightmap[1])):
                if adj_coord not in mapped_coordinates:
                    adj_x, adj_y = adj_coord
                    adj_height = heightmap[adj_x][adj_y]
                    if step_condition(tile_height, adj_height):
                        if result_condition(adj_coord):
                            return step_count
                        mapped_coordinates.add(adj_coord)
                        next_map_queue.append(adj_coord)

        gHandle = ctypes.windll.kernel32.GetStdHandle(ctypes.c_long(-11))
        ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, ctypes.c_ulong(0))
        print_str = ""
        for x, row in enumerate(heightmap):
            for y, char in enumerate(row):
                if (x, y) in mapped_coordinates:
                    print_str += "#"
                else:
                    print_str += " "
            print_str += "\n"
        print(print_str)
        time.sleep(0.01)

        current_map_queue = next_map_queue
        step_count += 1


def main():
    heightmap = []
    start_pos = ()
    end_pos = ()
    with open("day_12_input", "r") as f:
        a_ascii = ord("a")
        for x, line in enumerate(x.strip() for x in f):
            row = []
            for y, char in enumerate(line):
                if char == "S":
                    height = 0
                    start_pos = (x, y)
                elif char == "E":
                    height = 25
                    end_pos = (x, y)
                else:
                    height = ord(char) - a_ascii
                row.append(height)
            heightmap.append(row)

    print(count_steps(
        heightmap,
        start_pos,
        lambda current_height, next_height: next_height - 1 <= current_height,
        lambda tile_coord: tile_coord == end_pos
    ))
    print()
    time.sleep(2)
    print(count_steps(
        heightmap,
        end_pos,
        lambda current_height, next_height: next_height + 1 >= current_height,
        lambda tile_coord: heightmap[tile_coord[0]][tile_coord[1]] == 0
    ))


if __name__ == "__main__":
    main()
