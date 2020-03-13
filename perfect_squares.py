def numSquares_dp(n):
    """
    Dynamic programming (slow, time limit exceeded)
    Time: O(n*sqrt(n))
    Space: O(n)
    """
    from collections import defaultdict
    dp = defaultdict(int)
    # total time: int(sqrt(1)) + int(sqrt(2)) + ... + int(sqrt(n))
    # there will be (i+1)^2 - i^2 = 2i-1 repeating numbers between sqrt((i+1)^2) and sqrt(i^2)
    # The predominant term in the sum above is n*int(sqrt(n)), therefore O(n*sqrt(n))
    for i in range(1, n+1):
        # loop for n times
        dp[i] = i
        j = 1
        while i - j ** 2 >= 0:
            # loop for int(sqrt(i)) times, for every i
            dp[i] = min(dp[i], dp[i - j ** 2] + 1)
            j += 1
    return dp[n]


def numSquares(n):
    """
    Brute force recursion (slow, time limit exceeded)
    """
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
