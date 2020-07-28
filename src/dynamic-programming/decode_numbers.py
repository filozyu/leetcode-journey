def numDecodings(s):
    """
    Dynamic programming
    Time: O(n)
    Space: O(n)
    """
    if s == "" or s[0] == "0":
        return 0

    if len(s) == 1:
        return 1

    dp = [0] * len(s)
    dp[0] = 1

    if s[1] == "0":
        if s[0] >= 3:
            return 0
        else:
            dp[1] = 1
    elif 10 < int(s[0:2]) <= 26:
        dp[1] = 2
    else:
        dp[1] = 1

    for i in range(2, len(s)):
        if (s[i] == "0" and s[i - 1] == "0") or (int(s[i - 1]) > 2 and int(s[i]) == 0):
            return 0

        if s[i] == "0":
            # if the current num = 0 and the previous num <= 2
            # then the previous num and the current num has to form a letter together
            dp[i] = dp[i - 2]

        else:
            # if the current num is not 0
            # then itself can be a letter
            if s[i] != "0":
                dp[i] += dp[i - 1]
            # if the previous number and the current number form a number between 10 and 26
            # then the two of them can also be a letter
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2]

    return dp[len(s) - 1]


test = "230"
print(numDecodings(test))
