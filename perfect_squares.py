def numSquares(n):
    i = 2
    sq_list = []
    while i**2 <= n:
        sq_list.append(i**2)

        if i**2 == n:
            return 1

        i += 1

    return sum_in_list(n, sq_list)


def sum_in_list(summ, l):
    sublist = [i for i in l if i <= summ]
    min_num = summ
    if len(sublist) == 0:
        return summ
    for i in range(len(sublist)-1, -1, -1):
        curr_divide = sublist[i]
        excess = summ % curr_divide
        if 0 < excess < 4:
            new_len = excess + int(summ/curr_divide)
        elif excess == 0:
            new_len = int(summ/curr_divide)
        else:
            new_len = sum_in_list(excess, sublist[:-1]) + int(summ/curr_divide)
        if new_len < min_num:
            min_num = new_len
    return min_num

print(numSquares(10))