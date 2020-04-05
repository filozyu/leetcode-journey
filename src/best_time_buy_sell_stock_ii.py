def maxProfit(prices):
    """
    One pass
    Time: O(n)
    Space: O(n) (worst case e.g. [1, 100, 2, 100, 3, 100]) for buy and sell
    """
    buy = []
    sell = []
    for price in prices:
        if len(buy) > len(sell):
            if price > buy[-1]:
                sell.append(price)
                continue
            else:
                buy[-1] = price
                continue
        elif len(sell) == 0 or sell[-1] > price:
            buy.append(price)
        elif sell[-1] <= price:
            sell[-1] = price
    if len(buy) != len(sell):
        buy.pop()

    profit = sum([sell[i] - buy[i] for i in range(len(buy))])
    return profit


test = [7,6,4,3,1]
print(maxProfit(test))
