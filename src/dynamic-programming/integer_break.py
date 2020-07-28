def integerBreak(n):
    """
    Dynamic programming
    Time: O(n^2)
    Space: O(n)
    """
    # dp[i] contains the maximum product of summands of integer i
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        curr_max = 0
        for j in range(1, i):
            # for every integer, check all the integers smaller than it
            # NOTE: every integer should be broken into the sum of at least 2 positive integers
            # therefore i can be 1 + (i-1) or 2 + (i-2) ... i-1 + (i - (i-1))
            # for every j, dp[j] does not contain the solution of j + 0, so we need to get the max of the two first
            # then the product of i's summands can be calculated as follows
            if max(dp[j], j) * (i - j) > curr_max:
                curr_max = max(dp[j], j) * (i - j)
                dp[i] = curr_max

    return dp[n]


test = 10
print(integerBreak(test))
