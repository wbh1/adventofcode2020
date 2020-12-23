import collections as c
import itertools
import copy
import hashlib


def score(winner):
    score = 0
    for i in range(1, len(winner) + 1):
        score += winner.pop() * i
    return score


def play(player1, player2):
    p1 = player1.copy()
    p2 = player2.copy()
    done = False
    winner = None
    while not done:
        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if p1_card > p2_card:
            # print(f"Player 1 wins with {p1_card} vs {p2_card}.")
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            # print(f"Player 2 wins with {p1_card} vs {p2_card}.")
            p2.append(p2_card)
            p2.append(p1_card)

        if len(p1) == 0 or len(p2) == 0:
            done = True
            winner = p1 if len(p1) > 0 else p2

    return winner


def recurse_play(player1, player2):
    prev_rounds = {"p1": [], "p2": []}
    decks = {"p1": player1.copy(), "p2": player2.copy()}
    done = False
    winner = (None, None)
    while not done:
        p1 = decks["p1"]
        p2 = decks["p2"]
        """If there was a previous round in this game
        that had exactly the same cards in the same order in
        the same players' decks, the game instantly ends in a win for player 1."""
        if p1 in prev_rounds["p1"] or p2 in prev_rounds["p2"]:
            done = True
            winner = ("p1", p1)
            break
        else:
            prev_rounds["p1"].append(p1.copy())
            prev_rounds["p2"].append(p2.copy())

        p1_card = p1.popleft()
        p2_card = p2.popleft()

        if len(p1) >= p1_card and len(p2) >= p2_card:
            p1_sub = c.deque(itertools.islice(p1.copy(), p1_card))
            p2_sub = c.deque(itertools.islice(p2.copy(), p2_card))
            sub_winner = recurse_play(p1_sub, p2_sub)
            if sub_winner[0] == "p1":
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                p2.append(p2_card)
                p2.append(p1_card)
        else:
            if p1_card > p2_card:
                # print(f"Player 1 wins with {p1_card} vs {p2_card}.")
                p1.append(p1_card)
                p1.append(p2_card)
            else:
                # print(f"Player 2 wins with {p1_card} vs {p2_card}.")
                p2.append(p2_card)
                p2.append(p1_card)

        if len(p1) == 0 or len(p2) == 0:
            done = True
            winner = ("p1", p1) if len(p1) > 0 else ("p2", p2)
            break

    return winner


if __name__ == "__main__":
    puzzle_input = None
    with open("input.txt") as f:
        puzzle_input = f.read().split("\n\n")
        f.close()

    player1 = c.deque(int(i) for i in puzzle_input[0].split("\n")[1:])
    player2 = c.deque(int(i) for i in puzzle_input[1].split("\n")[1:])

    print("Part 1:", score(play(player1, player2)))
    print("Part 2:", score(recurse_play(player1, player2)[1]))