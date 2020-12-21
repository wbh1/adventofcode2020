import re
from math import sqrt
import pprint
from collections import Counter
import itertools

tile_id_re = re.compile(r"^Tile ([0-9]{4}):")
edges = {}


class Tile:
    def __init__(self, data):
        data = data.split("\n")
        self.id = tile_id_re.match(data[0]).group(1)
        self.contents = data[1:]
        self.edges = [
            self.contents[0],
            self.contents[1],
            "".join([x[0] for x in self.contents]),
            "".join([x[-1] for x in self.contents]),
        ]


puzzle_input = None
with open("test.txt") as f:
    puzzle_input = f.read().split("\n\n")
    f.close()

TILES = [Tile(t) for t in puzzle_input]
grid_size = int(sqrt(len(TILES)))
for t in TILES:
    for e in t.edges:
        rev = e[::-1]
        for x in [e, rev]:
            if x in edges.keys():
                edges[x].append(t.id)
            else:
                edges[x] = [t.id]

single_edges = Counter()
for edge, tiles in edges.items():
    if len(tiles) == 1 and len(edges[edge[::-1]]) == 1:
        single_edges.update(tiles)

print(single_edges)

grid = [[[] for _ in range(grid_size)] for _ in range(grid_size)]
# pprint.pprint(grid)

tile_frequency = Counter(itertools.chain.from_iterable(edges.values()))
# This is how many sides match
isolated = Counter()
for e, t in edges.items():
    if len(t) == 1:
        isolated.update(t)
