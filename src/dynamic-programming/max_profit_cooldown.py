def maxProfit(prices):
    """
    Dynamic programming
    Time: O(n) n - number of days
    Space: O(n) the recursion stack
    """

    def recur(day):
        if day == 0:
            return [-prices[0], 0, 0]

        # dp[0]: having stock at the END of this day
        # dp[1]: Sold stock by within this day, so the next day (day + 1) will be frozen
        # dp[2]: Have no stock and have not sold any at the END of this day

        dp = [0, 0, 0]

        prev_have, prev_sell, prev_empty = recur(day - 1)

        # having stock at the END of this day (impossible to be frozen)
        # 1) stock from the previous day (prev_have)
        # 2) bought this day, which means we did not sell nor buy the previous day (so prev_empty)
        dp[0] = max(prev_have, prev_empty - prices[day])

        # sold stock within this day
        # which implies we must have stock from the previous day
        dp[1] = prev_have + prices[day]

        # no stock and sold nothing this day
        # 1) sold the previous day (prev_sell) and now we are frozen
        # 2) did not have stock and did not sold either the previous day (prev_empty)
        dp[2] = max(prev_sell, prev_empty)

        return dp

    if len(prices) == 0:
        return 0

    res = recur(len(prices) - 1)
    return max(res)


test = [1, 2, 3, 0, 2]
print(maxProfit(test))
