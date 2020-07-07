def maxProfit(prices):
    """
    Brute force (Time Limit Exceeded)
    Time: O(n^2)
    Space: O(1)
    """
    max_profit = 0
    num_days = len(prices)
    for i in range(num_days):
        for j in range(i, num_days):
            curr_profit = prices[j] - prices[i]
            if curr_profit > max_profit:
                max_profit = curr_profit
    return max_profit


def maxProfit_dp(prices):
    """
    One pass, keep track of the minimum before the current day (similar to dynamic programming)
    Time: O(n)
    Space: O(1)
    """
    max_profit = 0
    num_days = len(prices)
    if num_days == 0:
        return 0
    min_price = prices[0]
    for i in range(1, num_days):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit


test = [7, 1, 5, 3, 6, 4]
print(maxProfit_dp(test))
