from copy import deepcopy
from functools import reduce
import operator


class Monkey:
    def __init__(self, starting_items, operation_f, test_divisible_by, target_true, target_false):
        self.items = starting_items
        self.operation_f = operation_f
        self.test_divisible_by = test_divisible_by
        self.target_true = target_true
        self.target_false = target_false
        self.inspect_count = 0

    def turn(self, monkeys, total_product, reduce_worry):
        for worry in self.items:
            self.inspect_count += 1
            worry = self.operation_f(worry)
            if reduce_worry:
                worry //= 3
            worry %= total_product
            target = self.target_false if worry % self.test_divisible_by else self.target_true
            monkeys[target].items.append(worry)
        self.items.clear()


def parse_monkey(file):
    starting_items = list(map(int, next(file).rstrip().removeprefix("  Starting items: ").split(", ")))
    operation_str = next(file).rstrip().removeprefix("  Operation: new = ")
    operation_f = eval(f"lambda old: {operation_str}")
    test_divisible_by = int(next(file).rstrip().removeprefix("  Test: divisible by "))
    true_throw_to = int(next(file).rstrip().removeprefix("    If true: throw to monkey "))
    false_throw_to = int(next(file).rstrip().removeprefix("    If false: throw to monkey "))

    return Monkey(starting_items, operation_f, test_divisible_by, true_throw_to, false_throw_to)


def main():
    monkeys = []
    with open("day_11_input", "r") as f:
        for line in f:
            if "Monkey" in line:
                monkeys.append(parse_monkey(f))

    test_product = reduce(operator.mul, (m.test_divisible_by for m in monkeys))

    monkeys_copy = deepcopy(monkeys)
    for _ in range(20):
        for monkey in monkeys_copy:
            monkey.turn(monkeys_copy, test_product, True)

    monkeys_copy.sort(key=lambda m: m.inspect_count)
    print(monkeys_copy[-1].inspect_count * monkeys_copy[-2].inspect_count)

    monkeys_copy = deepcopy(monkeys)
    for _ in range(10000):
        for monkey in monkeys_copy:
            monkey.turn(monkeys_copy, test_product, False)

    monkeys_copy.sort(key=lambda m: m.inspect_count)
    print()
    print(monkeys_copy[-1].inspect_count * monkeys_copy[-2].inspect_count)


if __name__ == "__main__":
    main()
