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
    print(list(sorted_waits.keys())[0].ID * list(sorted_waits.values())[0])


def part2(input):
    BUSSES = []
    for b in input[1].split(","):
        if b != "x":
            BUSSES.append(Bus(int(b)))
        else:
            BUSSES.append(None)
    """OK so.
    The first bus has an ID of 13.
    The second bus has an ID of 37.
    You can calculate when these busses overlap the way they are supposed to by finding x
        bus1 * x = T
        (T + offset) % bus2 = 0
    The only time they intercept is at multiples of T, so increase timestamp by that each time.
    """

    def lcm(denominators):
        from math import gcd
        from functools import reduce

        return reduce(lambda a, b: a * b // gcd(a, b), denominators)

    intervals = []
    starter_bus = BUSSES[0]
    for bus in BUSSES[1:]:
        if not bus:
            continue
        t_offset = BUSSES.index(bus)
        t = 0
        x = 0
        done = False
        while not done:
            t = starter_bus.ID * x
            done = (t + t_offset) % bus.ID == 0
            if not done:
                x += t_offset
            else:
                print(
                    f"{starter_bus.ID} and {bus.ID} align correctly every {t}s. Offset: {t_offset}"
                )
                intervals.append(t)

    print(lcm(intervals))

    # for bus in BUSSES:
    #     if not bus:
    #         continue
    #     next_bus = next(
    #         (b for b in BUSSES[BUSSES.index(bus) + 1 :] if b is not None), None
    #     )
    #     if not next_bus:
    #         break
    #     offset = BUSSES.index(next_bus) - BUSSES.index(bus)
    #     seconds_since_t = BUSSES.index(bus)

    #     done = False
    #     x = 0
    #     t = 0
    #     while not done:
    #         t = bus.ID * x
    #         done = (t + offset) % next_bus.ID == 0
    #         if not done:
    #             x += offset
    # else:
    #     print(f"{bus.ID} and {next_bus.ID} align correctly every {t}s. Offset: {offset}")
    #     intervals.append(t)

    # def lcm(denominators):
    #     from math import gcd
    #     from functools import reduce
    #     return reduce(lambda a, b: a * b // gcd(a, b), denominators)
    # print(lcm(intervals))


with open("input.txt") as f:
    input = f.read().splitlines()
    part1(input)
    # part2(input)

with open("test.txt") as f:
    input = f.read().splitlines()
    part2(input)
