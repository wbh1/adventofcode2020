def process(input: list):
    import string

    GROUP_YES_ANSWERS = []
    UNANINIMOUS_YES = []

    for group in input:
        question_answers = {
            key: 0 for key in list(string.ascii_lowercase)
        }  # Populate a dict by iterating over the alphabet.

        for member in group:
            for answer in member:
                question_answers[answer] += 1  # Increment by 1 for each yes answer

        yes_answers = unanimous = 0
        for value in question_answers.values():
            if value:
                yes_answers += 1

            if value == len(group):
                unanimous += 1

        GROUP_YES_ANSWERS.append(yes_answers)
        UNANINIMOUS_YES.append(unanimous)

    print(sum(GROUP_YES_ANSWERS), "is the number of yes's provided.")
    print(sum(UNANINIMOUS_YES), "is the number of unanimous yes's provided.")


def split_into_groups(input: list):
    GROUP_MEMBERS = []
    ALL_GROUPS = []

    for line in input:
        values = line.strip("\n")
        if values:  # Will be False if string is empty after removing new line
            GROUP_MEMBERS.append(values)
        else:
            ALL_GROUPS.append(GROUP_MEMBERS)  # flush the buffer to start a new group
            GROUP_MEMBERS = []

    # One last flush of the buffer
    ALL_GROUPS.append(GROUP_MEMBERS)

    return ALL_GROUPS


with open("input.txt") as f:
    input = f.read().splitlines()

    input = split_into_groups(input)
    print("OUTPUT:")
    process(input)

    f.close()
