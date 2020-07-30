def canPartition(nums):
    """
    Dynamic programming
    Time: O(s * n) n = len(nums); s = sum(nums)
    Space: O(s * n) space for dp
    """
    if len(nums) < 2:
        return False

    s = sum(nums)

    # we want a subset with sum being half of the sum(nums)
    # Note that such a subset cannot be nums itself since every number is positive
    if s % 2 == 1:
        return False
    else:
        s = int(s / 2)

    # dp[i][j] is
    # True if there is a subset in nums[0], ..., nums[i] such that the sum is j
    # False if not
    dp = [[False] * (s + 1) for _ in range(len(nums) + 1)]

    # default is 0 (pick 0 numbers to sum to 0)
    dp[0][0] = True

    for i in range(1, len(nums) + 1):
        for j in range(1, s + 1):

            # NOTE: here i starts from 1, to convert back to index in nums, use i-1
            # to choose from the first i numbers, we have two options:
            # 1) do not choose the i-th number, then dp[i][j] is the same as dp[i-1][j]
            # 2) choose the i-th number, then (j - nums[i-1]) > 0 must be formed by a subset from the first i-1 numbers
            # if either case is True, dp[i][j] is True

            if j - nums[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(nums)][s]


def canPartition_efficient(nums):
    """
    Dynamic programming 1D
    Time: O(s * n)
    Space: O(s)
    """
    if len(nums) < 2:
        return False

    s = sum(nums)

    # we want a subset with sum being half of the sum(nums)
    # Note that such a subset cannot be nums itself since every number is positive
    if s % 2 == 1:
        return False
    else:
        s = int(s / 2)

    # dp still stores whether any subset from nums[0], ..., nums[i] sums up to j
    # the whole dp array gets updated for every i
    dp = [False] * (s + 1)
    dp[0] = True

    for i in range(len(nums)):
        # NOTE: here we loop j from back ward since when we have 2D dp,
        # we need the current row and the previous row to fill in the value,
        # the values we want to fill in the current row (j) always refers to the left of the previous row (j-nums[i])\
        # so if we want to use just one row of dp, we need to update from the rear towards the beginning
        for j in range(s, 0, -1):

            if j >= nums[i]:
                # if j = nums[i], dp[j] = True
                dp[j] = dp[j] or dp[j - nums[i]]
            else:
                # otherwise there is no need to continue the current j loop, all other j < nums[i]
                break

    return dp[s]


test = [1, 5, 11, 5]
print(canPartition(test))
