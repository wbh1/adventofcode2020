import numpy
from scipy.ndimage import convolve
import copy

with open("input.txt") as f:
    """My brain was not super functional today,
    so I fully admit to borrowing heavily from other's designs.
    Sue me."""
    input_grid = numpy.array(
        [[i == "#" for i in line] for line in f.read().splitlines()]
    )
    for dimensions in range(3, 5):
        grid = copy.copy(input_grid)
        # we already have 2 dimensions, expand to fit the rest
        grid = numpy.expand_dims(grid, axis=tuple(range(dimensions - 2)))
        adjacents = numpy.ones(shape=(3,) * dimensions)
        # skip yourself
        adjacents[(1,) * dimensions] = 0

        for _ in range(6):
            # Expand the grid by 1 in all directions
            grid = numpy.pad(grid, 1).astype(int)
            # Convolve points on grid with the position of their adjacents
            convolution = convolve(grid, adjacents, mode="constant")
            grid = (grid == 1) & ((convolution == 2) | (convolution == 3)) | (
                grid == 0
            ) & (convolution == 3)

        print(numpy.sum(grid))
    f.close()
