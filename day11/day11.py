from copy import deepcopy


def adjacents(list, row, col):
    adj = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == y == 0:
                continue  # ignore yourself
            if 0 <= row + x < len(list) and 0 <= col + y < len(list[0]):
                if list[row + x][col + y] == "#":
                    adj += 1
    return adj


with open("input.txt") as f:
    input = f.read().splitlines()
    changed = True
    while changed:
        newL = deepcopy(input)
        changed = False
        for r_ind, row in enumerate(input):
            new_row = ""
            for c_ind, seat in enumerate(row):
                adj = adjacents(input, r_ind, c_ind)
                if seat == "L" and adj == 0:
                    changed = True
                    new_row += "#"
                elif seat == "#" and adj >= 4:
                    changed = True
                    new_row += "L"
                else:
                    new_row += seat  # nothing to change
            newL[r_ind] = new_row
        input = newL
    occ = 0
    for row in input:
        for s in row:
            if s == "#":
                occ += 1
    print(occ)