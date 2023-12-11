from day23.day23 import solve_updated

test_input = [int(i) for i in "389125467"]

def test_part1():
    # cups = solve(test_input)
    # assert exp == int("".join(str(n) for n in sort(cups)))
    assert 92658374 == int(solve_updated(test_input, moves=10))
    assert 67384529 == int(solve_updated(test_input))

def test_part2():
    assert 149245887792 == solve_updated(test_input, moves=10000000)
