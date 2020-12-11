from copy import deepcopy


def adjacents(list, row, col, part1: bool):
    adj = []
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue  # ignore yourself
            if part1:
                if 0 <= row + x < len(list) and 0 <= col + y < len(list[0]):
                    adj.append(list[row + x][col + y])
            else:
                i = 1
                while 0 <= row + x * i < len(list) and 0 <= col + y * i < len(list[0]):
                    seat = list[row + x * i][col + y * i]
                    if seat != ".":
                        adj.append(seat)
                        break
                    i += 1
    return adj.count("#")


def shuffle(input, adjacents_allowed):
    part1 = adjacents_allowed == 4
    changed = True
    while changed:
        newL = deepcopy(input)
        changed = False
        for r_ind, row in enumerate(input):
            new_row = ""
            for c_ind, seat in enumerate(row):
                adj = adjacents(input, r_ind, c_ind, part1)
                if seat == "L" and adj == 0:
                    changed = True
                    new_row += "#"
                elif seat == "#" and adj >= adjacents_allowed:
                    changed = True
                    new_row += "L"
                else:
                    new_row += seat  # nothing to change
            newL[r_ind] = new_row
        input = newL

    return input


def output(input):
    occ = 0
    for row in input:
        occ += row.count("#")
    print(occ)


with open("input.txt") as f:
    input = f.read().splitlines()
    p1 = shuffle(input, 4)
    output(p1)
    p2 = shuffle(input, 5)
    output(p2)
