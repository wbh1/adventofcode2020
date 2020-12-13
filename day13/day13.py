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
            BUSSES.append(Bus(1))
    """OK so.
    The first bus has an ID of 13.
    The second bus has an ID of 37.
    You can calculate when these busses overlap the way they are supposed
    by finding the LCM of bus1 and bus2+offset
    bus1 * x = T
    bus2 will be divisible into T + offset
    """
    from math import gcd
    from functools import reduce

    def lcm(denominators):
        return reduce(lambda a, b: a * b // gcd(a, b), denominators)
    
    b_ids = [b.ID for b in BUSSES]
    print(lcm(b_ids))

    # TS = 100000000000000
    # for i1, bus1 in enumerate(BUSSES):
    #     if bus1 == "x":
    #         continue
    #     next_bus = next((b for b in BUSSES[BUSSES.index(bus1) + 1 :] if b != "x"), None)
    #     if not next_bus:
    #         break
    #     offset = BUSSES.index(next_bus) - i1
    #     done = False
    #     while not done:
    #         done = ((bus1.ID * TS) + offset) % next_bus.ID == 0
    #         if not done:
    #             TS += 1
    #     print(TS)


with open("input.txt") as f:
    input = f.read().splitlines()
    part1(input)
    # part2(input)

with open("test.txt") as f:
    input = f.read().splitlines()
    part2(input)