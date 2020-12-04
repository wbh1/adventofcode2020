def valid_password_part1(line: str) -> bool:
    occurence_criteria = line.split(" ")[0]
    letter_criteria = line.split(" ")[1].strip(":")  # Remove the trailing colon
    password = line.split(" ")[2]

    min_occurence = int(occurence_criteria.split("-")[0])
    max_occurence = int(occurence_criteria.split("-")[1])

    letter_occurences = 0

    for letter in password:
        if letter == letter_criteria:
            letter_occurences += 1

    if letter_occurences >= min_occurence and letter_occurences <= max_occurence:
        return True

    return False


def valid_password_part2(line: str) -> bool:
    occurence_criteria = line.split(" ")[0]
    letter_criteria = line.split(" ")[1].strip(":")  # Remove the trailing colon
    password = line.split(" ")[2]

    first_letter_index = int(occurence_criteria.split("-")[0])
    last_letter_index = int(occurence_criteria.split("-")[1])

    if (
        letter_criteria == password[first_letter_index - 1]
        and letter_criteria != password[last_letter_index - 1]
    ) or (
        letter_criteria != password[first_letter_index - 1]
        and letter_criteria == password[last_letter_index - 1]
    ):
        return True

    return False


def part1(input: list):
    valid_passwords_count = 0
    for password in input:
        if valid_password_part1(password):
            valid_passwords_count += 1

    print(valid_passwords_count, "valid passwords.")


def part2(input: list):
    valid_passwords_count = 0
    for password in input:
        if valid_password_part2(password):
            valid_passwords_count += 1

    print(valid_passwords_count, "valid passwords.")


with open("input.txt") as f:
    input = f.read().splitlines()

    print("PART 1:")
    part1(input)
    print("PART 2:")
    part2(input)

    f.close()
