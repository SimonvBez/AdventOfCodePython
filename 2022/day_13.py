import ast
from functools import reduce
from operator import mul


def compare_pair(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif isinstance(left, list) and isinstance(right, list):
        if not left and not right:
            return None
        elif not left:
            return True
        elif not right:
            return False
        left_val, *left_rest = left
        right_val, *right_rest = right
        if (result := compare_pair(left_val, right_val)) is not None:
            return result
        else:
            return compare_pair(left_rest, right_rest)
    else:
        if isinstance(left, int):
            return compare_pair([left], right)
        else:
            return compare_pair(left, [right])


def main():
    pairs = []
    all_packets = []

    with open("day_13_input", "r") as f:
        pair = []
        for line in (x.strip() for x in f):
            if line:
                packet = ast.literal_eval(line)
                pair.append(packet)
                all_packets.append(packet)
            else:
                pairs.append(pair)
                pair = []

    indices_sum = 0
    for i, pair in enumerate(pairs):
        if compare_pair(*pair):
            indices_sum += i + 1

    print(indices_sum)

    divider_packets = ([[2]], [[6]])
    all_packets.extend(divider_packets)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(all_packets)-1):
            left = all_packets[i]
            right = all_packets[i+1]
            if not compare_pair(left, right):
                all_packets[i], all_packets[i+1] = all_packets[i+1], all_packets[i]
                is_sorted = False

    print()
    decoder_key = reduce(mul, (all_packets.index(packet) + 1 for packet in divider_packets))
    print(decoder_key)


if __name__ == '__main__':
    main()
