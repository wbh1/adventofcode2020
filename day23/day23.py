puzzle_input = [int(i) for i in "476138259"]
test_input = [int(i) for i in "389125467"]


def next_index(last_index):
    if last_index == len(puzzle_input) - 1:
        return 0
    else:
        return last_index + 1


def next_cup_indices(index):
    indices = []
    max_index = len(puzzle_input)
    for n in range(1, 4):
        indices.append((index + n) % max_index)
    return indices


def solve(data):
    cups = data.copy()
    cur_cup = cups[8]
    move = 1
    for _ in range(100):
        """-- move 1 --
        cups: (3) 8  9  1  2  5  4  6  7
        pick up: 8, 9, 1
        destination: 2"""
        cur_cup = cups[next_index(cups.index(cur_cup))]
        print(f"-- move {move} --")
        print(
            "cups:", " ".join([str(n) for n in cups]).replace(str(cur_cup), f"({cur_cup})")
        )
        next_cups = [cups[i] for i in next_cup_indices(cups.index(cur_cup))]
        print("pick up:", ", ".join(str(n) for n in next_cups))
        for c in next_cups:
            cups.remove(c)

        dest_cup = cur_cup - 1
        while dest_cup not in cups:
            if dest_cup <= 0:
                dest_cup = max(cups)
                continue
            else:
                dest_cup -= 1
        print("destination:", dest_cup, "\n")
        dest_index = cups.index(dest_cup)
        for c in next_cups:
            dest_index += 1
            cups.insert(dest_index, c)
        move += 1

    return cups


def sort(cups: list):
    split = cups.index(1)
    pre = cups[:split]
    post = cups[split + 1 :]
    return post + pre


cups = solve(puzzle_input)
print("Part 1:", "".join(str(n) for n in sort(cups)))
