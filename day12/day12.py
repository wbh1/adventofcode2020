class Ship:
    def __init__(self, initial_heading):
        self.heading = initial_heading
        self.x = 0
        self.y = 0

    def move(self, instruction):
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
            self.move(new_instruction)

    def _rotate(self, direction, units):
        headings = list("NESW")
        turns = units / 90
        new_index = headings.index(self.heading)
        if direction == "L":
            new_index -= turns
        elif direction == "R":
            new_index += turns

        if new_index >= len(headings) or new_index < 0:
            new_index = new_index % len(headings)

        new_index = int(new_index)

        self.heading = headings[new_index]

    def manhattan_dist(self):
        return abs(self.x) + abs(self.y)


with open("input.txt") as f:
    input = f.read().splitlines()
    boat = Ship("E")
    for line in input:
        boat.move(line)
    print(boat.manhattan_dist())