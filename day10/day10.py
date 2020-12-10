class Adapter:
    def __init__(self, joltage):
        self.joltage = joltage

    def connect(self, source_adapter):
        MAX_DIFF = 3
        difference = abs(self.joltage - source_adapter.joltage)
        if difference > MAX_DIFF:
            raise ValueError("Difference in joltages is too high")
        else:
            return difference


def part1(starting_adapter, adapter_list):
    DIFFERENCES = {number: 0 for number in range(1, 4)}
    while adapter_list:
        a = adapter_list.pop(0)
        DIFFERENCES[a.connect(starting_adapter)] += 1
        starting_adapter = a

    return DIFFERENCES


def part2(adapter_list):
    # If we know how to reach n-1, n-2, and n-3, then we know that the sum of the # of ways to reach each of those
    # is the number of ways to reach n. Only up to 3 since that's how much variance is allowed for.
    from collections import Counter

    joltage_list = [a.joltage for a in adapter_list]
    variations = Counter()

    # Give an initial value since there is 1 way to reach the first number
    variations[0] = 1

    for j in joltage_list:
        variations[j] = variations[j - 1] + variations[j - 2] + variations[j - 3]

    # return the number of variations on the last # in the joltage list
    return variations[joltage_list[-1]]


with open("input.txt") as f:
    input = [int(line) for line in f.read().splitlines()]
    input.sort()  # Sorting the input makes iterating easier since we know what connects to what
    ADAPTERS = [Adapter(a) for a in input]
    ADAPTERS.append(Adapter(max(input) + 3))  # Append my device to list of Adapters

    DIFFERENCES = part1(Adapter(0), ADAPTERS.copy())
    print(DIFFERENCES)

    print("Part 1:", DIFFERENCES[1] * DIFFERENCES[3])
    print(part2(ADAPTERS))
    # perms = tree(Adapter(0), [], ADAPTERS)
