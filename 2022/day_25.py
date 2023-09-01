def snafu_to_int(snafu_str):
    result = 0
    for i, digit_str in enumerate(reversed(snafu_str)):
        if digit_str == "=":
            digit = -2
        elif digit_str == "-":
            digit = -1
        else:
            digit = int(digit_str)
        result += digit * 5**i
    return result


def int_to_snafu(number):
    result = ""
    while number:
        number, digit = divmod(number, 5)
        if digit == 4:
            digit_str = "-"
            number += 1
        elif digit == 3:
            digit_str = "="
            number += 1
        else:
            digit_str = str(digit)

        result = digit_str + result
    return result


def main():
    numbers = []
    with open("day_25_input", "r") as f:
        for line in (x.rstrip() for x in f):
            numbers.append(snafu_to_int(line))

    print(int_to_snafu(sum(numbers)))


if __name__ == "__main__":
    main()
