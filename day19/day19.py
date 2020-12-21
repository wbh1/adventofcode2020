import re

puzzle_input = None
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()
    f.close()

RULES = {line.split(": ")[0]: line.split(": ")[1] for line in puzzle_input[:135]}
MESSAGES = puzzle_input[136:]


# This generates a disgusting regex
def match_rule(rule_id, part2=False):
    if part2:
        if rule_id == "8":
            # New rule 8 is simplified as just rule 42 one or more times
            return match_rule("42") + "+"
        if rule_id == "11":
            r42 = match_rule("42")
            r31 = match_rule("31")
            return (
                "(?:"
                + "|".join(
                    "{0}{1}{2}{1}".format(r42, "{" + str(n) + "}", r31)
                    for n in range(1, 10)
                )
                + ")"
            )

    rule = RULES[rule_id]
    if '"' in rule:
        return rule[1]

    _split = rule.split(" | ")
    result = []
    for side in _split:
        nums = side.split(" ")
        result.append("".join(match_rule(r, part2=part2) for r in nums))
    # '?:' means match everything inside
    return "(?:" + "|".join(result) + ")"


def part1():
    reg = match_rule("0")

    matches = 0
    for m in MESSAGES:
        matches += 1 if re.fullmatch(reg, m) else 0

    print(matches)


def part2():
    RULES["8"] = "42 | 42 8"
    RULES["11"] = "42 31 | 42 11 31"
    reg = match_rule("0", part2=True)
    print(reg)

    matches = 0
    for m in MESSAGES:
        matches += 1 if re.fullmatch(reg, m) else 0

    print(matches)


part1()
part2()
