def part1(numbers: list):
    for number1 in numbers:
        for number2 in numbers:
            if number1 is not number2 and number1 + number2 == 2020:
                print(number1, number2, "are your winners.")
                print(number1 * number2, "is their product.")
                return


def part2(numbers: list):
    for number1 in numbers:
        for number2 in numbers:
            if number1 is not number2:
                for number3 in numbers:
                    if number3 is not number2 and number1 + number2 + number3 == 2020:
                        print(number1, number2, number3, "are your winners.")
                        print(number1 * number2 * number3, "is their product.")
                        return


with open("input.txt") as f:
    input = f.read().splitlines()
    numbers = [int(x) for x in input]
    print("PART 1:")
    part1(numbers)
    print("PART 2:")
    part2(numbers)

    f.close()
