from typing import List

puzzle_input = [int(i) for i in "476138259"]


class Cups:
    def __init__(self, cups: List[int], total_cups=0):
        self.head: Cup
        c = Cup(label=cups[0])
        self.head = c
        self.values = {c.label: c}
        for x in cups[1:]:
            c.next = Cup(x)
            c = c.next
            self.values[c.label] = c
        if total_cups > len(cups):
            for x in range(len(cups) + 1, total_cups + 1):
                c.next = Cup(x)
                c = c.next
                self.values[c.label] = c

        c.next = self.head


class Cup:
    def __init__(self, label: int):
        self.label = label
        self.next: Cup


def solve_updated(data: List[int], moves=100):
    if moves > 100:
        linked_list = Cups(data, total_cups=1000000)
    else:
        linked_list = Cups(data)
    current_cup = linked_list.head

    for m in range(1, moves + 1):
        cursor = current_cup
        pickups = []
        for _ in range(0, 3):
            pickups.append(cursor.next)
            cursor = cursor.next
            if cursor.label == linked_list.head.label:
                linked_list.head = linked_list.head.next

        current_cup.next = cursor.next
        destination = current_cup.label - 1
        if destination < 1:
            destination = len(linked_list.values.keys())
        while linked_list.values[destination] in pickups:
            destination -= 1
            if destination < 1:
                destination = len(linked_list.values.keys())
        destination_cup = linked_list.values[destination]

        dest_next = destination_cup.next
        destination_cup.next = pickups[0]
        pickups[2].next = dest_next
        if destination_cup.label == linked_list.head.label:
            linked_list.head = pickups[2]
        current_cup = current_cup.next

    res = ""
    cup1: Cup = linked_list.values[1]
    if moves <= 100:
        cursor = cup1.next
        for _ in range(1, len(data)):
            res += str(cursor.label)
            cursor = cursor.next
        return res
    else:
        return cup1.next.label * cup1.next.next.label


def sort(cups: list):
    split = cups.index(1)
    pre = cups[:split]
    post = cups[split + 1 :]
    return post + pre


if __name__ == "__main__":
    cups = solve_updated(puzzle_input)
    print("Part 1:", cups)
    print("Part 2:", solve_updated(puzzle_input, 10000000))
