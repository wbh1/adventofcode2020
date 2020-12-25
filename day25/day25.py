CARD_PUB_KEY = 8458505
DOOR_PUB_KEY = 16050997

# Test inputs
# CARD_PUB_KEY = 17807724
# DOOR_PUB_KEY = 5764801


def transform(subj_num, loops):
    return pow(subj_num, loops, 20201227)


def brute_force(expected_result):

    res = 0
    loops = 0
    while res != expected_result:
        loops += 1
        res = transform(7, loops)
        # print(f"Attempt #{loops}:", res, expected_result)

    return loops

# This takes longer than door_loops to calculate, so don't.
# card_loops = brute_force(CARD_PUB_KEY)
door_loops = brute_force(DOOR_PUB_KEY)

encryption_key = transform(CARD_PUB_KEY, door_loops)

print(encryption_key)