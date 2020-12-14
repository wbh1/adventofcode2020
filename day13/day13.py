class Bus:
    def __init__(self, ID):
        self.ID = ID

    def next_arriving(self, timestamp):
        return timestamp % self.ID


def part1(input):
    earliest_departure = int(input[0])
    BUSSES = [Bus(int(b)) for b in input[1].split(",") if b != "x"]
    waittimes = {}
    for bus in BUSSES:
        waittimes[bus] = 0
        while bus.next_arriving(earliest_departure + waittimes[bus]) != 0:
            waittimes[bus] += 1
    sorted_waits = {
        k: v for k, v in sorted(waittimes.items(), key=lambda item: item[1])
    }
    print("Part 1:", list(sorted_waits.keys())[0].ID * list(sorted_waits.values())[0])


def part2(input):
    from itertools import count

    ts = int(input[0])  # earliest departure time

    input = [int(x) if x != "x" else x for x in input[1].split(",")]
    buses = tuple((i, b) for i, b in enumerate(input) if b != "x")

    step = 1
    """Starting at the earliest departure time,
    count forwards by `step`, setting the timestamp `ts` to the value
    in which the timestamp + the index of the bus align correctly.
    That is to say, in which the timestamp + the bus's offset
    divided by the bus's index leaves a remainder of 0.

    After finding the timestamp for one bus, proceed to the next one
    but first set the step that you are iterating by to be the previous
    step multiplied by the bus's ID since that bus will only fulfill
    the criteria described above at every `step` seconds. This greatly
    improves the run time of the program.

    To be honest, this still turns my brain into knots and my solution
    was heavily influenced by hints I found online. Supposedly this
    can be solved using Chinese Remainder Theorem but I don't know that.
    """
    for i, b in buses:
        ts = next(c for c in count(ts, step) if (c + i) % b == 0)
        step *= b
    print("Part 2:", ts)


with open("input.txt") as f:
    input = f.read().splitlines()
    part1(input)
    part2(input)
