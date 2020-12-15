spoken_nums = [20, 0, 1, 11, 6, 3]
next_num = 0
for loop in range(len(spoken_nums), 2020):
    prev_num = spoken_nums[loop - 1]
    if spoken_nums.count(prev_num) == 1:
        next_num = 0
    else:
        indices_of_prev_num = [
            i for i in range(len(spoken_nums)) if spoken_nums[i] == prev_num
        ]
        indices_of_prev_num.sort()
        last_occ = indices_of_prev_num[-1] + 1
        second_last_occ = indices_of_prev_num[-2] + 1
        next_num = last_occ - second_last_occ

    spoken_nums.append(next_num)

print(spoken_nums[-1])