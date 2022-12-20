class Number:
    # Number class to guarantee that every number is its own separate instance
    def __init__(self, value):
        self.value = value


def mix_numbers(numbers, original_order):
    for number_to_move in original_order:
        index = numbers.index(number_to_move)
        del numbers[index]
        insert_index = (number_to_move.value + index) % len(numbers)
        numbers.insert(insert_index, number_to_move)


def main():
    numbers = []
    with open("day_20_input", "r") as f:
        for line in (x.strip() for x in f):
            numbers.append(Number(int(line)))

    numbers_original = numbers.copy()

    mix_numbers(numbers, numbers_original)
    index_0 = next(i for i in range(len(numbers)) if numbers[i].value == 0)
    print(sum(numbers[i % len(numbers)].value for i in range(index_0, index_0+3001, 1000)))

    numbers = numbers_original.copy()
    for number in numbers:
        number.value *= 811589153

    for _ in range(10):
        mix_numbers(numbers, numbers_original)

    index_0 = next(i for i in range(len(numbers)) if numbers[i].value == 0)
    print(sum(numbers[i % len(numbers)].value for i in range(index_0, index_0+3001, 1000)))


if __name__ == "__main__":
    main()
