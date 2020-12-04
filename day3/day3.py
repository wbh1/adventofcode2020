def process(input: list, x_slope: int, y_slope: int):
    map = [list(row) for row in input]
    x = y = trees_hit = 0
    x_max = len(map[0]) - 1
    y_max = len(map) - 1
    # print(f"X max: {x_max}; Y max: {y_max}")

    x = x + x_slope
    y = y + y_slope

    while y <= y_max:
        if hit_tree(map, x, y):
            trees_hit += 1
            map[y][x] = "X"
        else:
            map[y][x] = "O"

        x = x + x_slope
        if x > x_max:
            x = x - x_max - 1  # re-zero the index by subtracting 1

        y = y + y_slope

    print(trees_hit, f"trees hit in a slope of ({x_slope}, {y_slope})")
    return trees_hit
    # print(f"Final coordinates: ({x}, {y})")


def hit_tree(map, x, y) -> bool:
    return map[y][x] == "#"


def part2(input: list):
    slopes = [
        {"x": 1, "y": 1},
        {"x": 3, "y": 1},
        {"x": 5, "y": 1},
        {"x": 7, "y": 1},
        {"x": 1, "y": 2},
    ]
    hits = []
    for slope in slopes:
        hits.append(process(input, slope["x"], slope["y"]))

    result = 1
    for hit in hits:
        result = result * hit

    print(result, "is your result.")


with open("input.txt") as f:
    input = f.read().splitlines()

    print("PART 1:")
    process(input, 3, 1)
    print("PART 2:")
    part2(input)

    f.close()
