import re


class Hexagon:
    BLACK = 0
    WHITE = 1

    def __init__(self, color=BLACK):
        self.color = color

    def flip(self):
        self.color = self.WHITE if self.color == self.BLACK else self.BLACK


def even(coordinate):
    # mod2 is implicit false if even b/c it's 0. invert.
    return not coordinate % 2


def get_coordinates(steps):
    """These directions are given in your list,
    respectively, as e, se, sw, w, nw, and ne.

    “even-r” horizontal layout
    shoves even rows right"""
    x = y = 0
    for s in steps:
        if s == "e":
            x += 1
        elif s == "se":
            if even(y):
                y += 1
                x += 1
            else:
                y += 1
        elif s == "sw":
            if even(y):
                y += 1
            else:
                x -= 1
                y += 1
        elif s == "w":
            x -= 1
        elif s == "nw":
            if even(y):
                y -= 1
            else:
                x -= 1
                y -= 1
        elif s == "ne":
            if even(y):
                y -= 1
                x += 1
            else:
                y -= 1

    return (x, y)


def populate_grid(puzzle_input):
    # https://www.redblobgames.com/grids/hexagons/#coordinates
    GRIDDY = {}

    steps = r"(e|se|sw|w|nw|ne)+?"
    step_re = re.compile(steps)

    for h in puzzle_input:
        steps = step_re.findall(h)
        hex_coord = get_coordinates(steps)
        if hex_coord in GRIDDY.keys():
            GRIDDY[hex_coord].flip()
        else:
            GRIDDY[hex_coord] = Hexagon()

    return GRIDDY


def count_black_tiles(GRIDDY):
    blacks = 0
    for H in GRIDDY.values():
        blacks += 1 if H.color == Hexagon.BLACK else 0
    return blacks


def flipadelphia(GRIDDY):
    """Any black tile with zero or more than 2 black tiles
    immediately adjacent to it is flipped to white.

    Any white tile with exactly 2 black tiles
    immediately adjacent to it is flipped to black."""
    import collections

    # A three-coordinate system would've resulted in less lines of code,
    # but more work for me to rewrite, so here we are.
    even_y_adj_mods = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, -1),
    ]

    odd_y_adj_mods = [
        (1, 0),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
    ]

    black_tiles = set(
        [coord for coord, hexagon in GRIDDY.items() if hexagon.color == Hexagon.BLACK]
    )

    for _ in range(100):
        _new_bt = set()
        whiteys = collections.defaultdict(int)
        for bt in black_tiles:
            _new_bt.add(bt)
            adjacentBlacks = 0
            adj_mods = even_y_adj_mods if even(bt[1]) else odd_y_adj_mods
            for adj_coord in [tuple(sum(x) for x in zip(bt, mod)) for mod in adj_mods]:
                if adj_coord in black_tiles:
                    adjacentBlacks += 1
                else:
                    # If the coordinate isn't in the set of black tiles,
                    # it must be white
                    whiteys[adj_coord] += 1
            if adjacentBlacks == 0 or adjacentBlacks > 2:
                _new_bt.remove(bt)

        for w, v in whiteys.items():
            if v == 2:
                _new_bt.add(w)
        black_tiles = _new_bt

    return len(black_tiles)


if __name__ == "__main__":
    puzzle_input = None
    with open("input.txt") as f:
        puzzle_input = f.read().splitlines()
        f.close()

    GRID = populate_grid(puzzle_input)

    print("Part 1:", count_black_tiles(GRID))

    print("Part 2:", flipadelphia(GRID))
