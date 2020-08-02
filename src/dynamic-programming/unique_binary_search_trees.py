def numTrees(n):
    """
    Dynamic programming
    Time: O(n^2)
    Space: O(n)
    """
    # dp[i] contains the number of unique binary search trees of sequence of length i
    dp = [0] * (n + 1)

    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        # for a sequence of length i (1, ..., i)
        # we can choose any number as the root
        # dp[i] is the sum of all unique BSTs with roots from 1 to i
        for j in range(1, i + 1):
            # if j is the root now,
            # all numbers < j (j-1 numbers) will be in the left branch of j
            # dp[j-1] records the unique number of BST for the left branch
            # all numbers > j (i-j numbers) will be in the right branch of j
            # dp[i-j] records the unique number of BST for the right branch
            # every possible BST for the left branch can pair with any possible BST for the right branch
            # therefore the product
            dp[i] += dp[j - 1] * dp[i - j]

    return dp[n]


test = 7
print(numTrees(test))
