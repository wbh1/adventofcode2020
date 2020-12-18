import pyparsing as pp

operand = pp.pyparsing_common.integer
allOps = pp.oneOf("+ - / *")
multOps = pp.oneOf("/ *")
addOps = pp.oneOf("+ -")

expr_part1 = pp.infixNotation(operand, [(allOps, 2, pp.opAssoc.LEFT)])

# Operator precedence is determined by order in the tuple list
expr_part2 = pp.infixNotation(
    operand, [(addOps, 2, pp.opAssoc.LEFT), (multOps, 2, pp.opAssoc.LEFT)]
)


def solve_problem(problem: pp.ParseResults):
    subgroups = []
    for subgroup in problem:
        if isinstance(subgroup, pp.ParseResults):
            subgroups.append(solve_problem(subgroup))
        else:
            subgroups.append(subgroup)

    # Must be >= 3 in order to have enough numbers to work on
    while len(subgroups) >= 3:
        # Get a number, an operator, and another number. Do math on it.
        # Use the map function to create a string version of each input first.
        res = eval("".join(map(str, subgroups[0:3])))
        # Replace the input with the result in the subgroups list
        subgroups = [res] + subgroups[3:]
    return int(subgroups[0])


puzzle_input = None
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()
    f.close()

print("Part 1:", sum([solve_problem(expr_part1.parseString(p)) for p in puzzle_input]))
print("Part 2:", sum([solve_problem(expr_part2.parseString(p)) for p in puzzle_input]))
