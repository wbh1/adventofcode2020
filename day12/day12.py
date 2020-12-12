class Ship:
    def __init__(self, initial_heading):
        self.heading = initial_heading
        self.waypoint = (10, 1)
        self.x = 0
        self.y = 0

    def part1(self, instruction):
        dir = instruction[:1]
        units = int(instruction[1:])
        if dir == "L" or dir == "R":
            self._rotate(dir, units)
        elif dir == "N":
            self.y += units
        elif dir == "S":
            self.y -= units
        elif dir == "E":
            self.x += units
        elif dir == "W":
            self.x -= units
        elif dir == "F":
            new_instruction = instruction.replace(dir, self.heading)
            self.part1(new_instruction)

    def _rotate(self, direction, units):
        headings = list("NESW")
        turns = units / 90
        new_index = headings.index(self.heading)
        if direction == "L":
            new_index -= turns
        elif direction == "R":
            new_index += turns

        if new_index >= len(headings):
            new_index = new_index % len(headings)

        new_index = int(new_index)

        self.heading = headings[new_index]

    def part2(self, instruction):
        dir = instruction[:1]
        units = int(instruction[1:])
        if dir == "L" or dir == "R":
            self._rotate_waypoint(dir, units)
        elif dir == "N":
            x, y = self.waypoint
            self.waypoint = (x, y + units)
        elif dir == "S":
            x, y = self.waypoint
            self.waypoint = (x, y - units)
        elif dir == "E":
            x, y = self.waypoint
            self.waypoint = (x + units, y)
        elif dir == "W":
            x, y = self.waypoint
            self.waypoint = (x - units, y)
        elif dir == "F":
            self.x += self.waypoint[0] * units
            self.y += self.waypoint[1] * units

    def _rotate_waypoint(self, direction, degrees):
        """For each 90deg rotation, the rotation
        flips x and y, and the new y is the negative of the old x.
        (x, y) = (y, -x)
        For each -90deg rotation, the rotation
        flips x and y, and the new x is the negative of the old y.
        (x, y) = (-y, x)"""
        turns = int(degrees / 90)
        for turn in range(turns):
            x, y = self.waypoint
            self.waypoint = (
                y if direction == "R" else -y,
                x if direction == "L" else -x,
            )

    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)


with open("input.txt") as f:
    input = f.read().splitlines()
    p1 = Ship("E")
    for line in input:
        p1.part1(line)
    print(p1.manhattan_dist())
    p2 = Ship("E")
    for line in input:
        p2.part2(line)
    print(p2.manhattan_dist())
