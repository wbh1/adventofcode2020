for i in [2020, 30000000]:
    spoken_nums = {k: [i] for i, k in enumerate([20, 0, 1, 11, 6, 3])}
    next_num = list(spoken_nums.keys())[-1]
    for loop in range(len(spoken_nums.keys()), i):
        """Keeping the try/except in the else block
        speeds it up by about 5s."""
        if len(spoken_nums[next_num]) == 1:
            next_num = 0
            spoken_nums[next_num].append(loop)
        else:
            # Next number is the most recent occurence of a number, minus
            # the second most recent occurrence of a number
            next_num = spoken_nums[next_num][-1] - spoken_nums[next_num][-2]
            try:
                spoken_nums[next_num].append(loop)
            except KeyError:
                spoken_nums[next_num] = [loop]

    print(next_num)
