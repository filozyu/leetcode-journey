def coinChange_memo(coins, amount):
    """
    Recursion with memorisation (top down)
    Time: O(n * a) n - length of coins, a - amount
    Space: O(a) for memo and the recursion stack
    """
    # memo[i] records the minimum number of coins needed for amount i

    def recur_memo(curr_amt):
        # no solution if curr_mat < 0
        if curr_amt < 0:
            return -1

        # if curr_amt is already 0, we don't need any coin
        if curr_amt == 0:
            return 0

        # if we have already calculated this node, return it
        # (nodes that have not been calculated have an initialised value of 0)
        if memo[curr_amt] != 0:
            return memo[curr_amt]

        # compute for the current node
        curr_min = float("inf")

        for c in coins:
            # note res could be less than 0 (when curr_amt < c)
            res = recur_memo(curr_amt - c)
            # if res = 0 that means c is the only coin we need to get curr_amt,
            # so curr_min = res + 1 = 1
            if res >= 0 and res + 1 < curr_min:
                # 1 for the current coin c
                curr_min = res + 1

        if curr_min == float("inf"):
            # if curr_min has not been updated at all
            # which means every res is -1 i.e. curr_amt cannot be made up using the existing coins
            memo[curr_amt] = -1

        else:
            # otherwise write the results of the current node to memo
            memo[curr_amt] = curr_min

        return recur_memo(curr_amt)

    if amount < 1:
        return 0

    memo = [0] * (amount + 1)

    return recur_memo(amount)


def coinChange(coins, amount):
    """
    Dynamic programming (bottom up)
    Time: O(n * a) n - length of coins, a - amount
    Space: O(a) space for dp
    """
    # dp[i] records the minimum number of coins needed for amount i
    dp = [float("inf")] * (amount + 1)

    # no coin is needed if amount is 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            # only update if the current amount >= c
            if i - c >= 0:
                # update dp[i] is dp[i - c] + 1 gives a better solution
                dp[i] = min(dp[i], dp[i - c] + 1)

    if dp[amount] == float("inf"):
        # no solution
        return -1
    else:
        return dp[amount]


test_coin = [1, 2, 5]
test_amt = 11
print(coinChange(test_coin, test_amt))
