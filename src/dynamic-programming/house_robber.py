def rob(nums):
    """
    Dynamic programming
    Time: O(n)
    Space: O(n)
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    # dp[i] contains the max profit at step i
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

    return dp[len(nums) - 1]


def rob_efficient(nums):
    """
    Dynamic programming with no extra space
    Time: O(n)
    Space: O(1)
    """
    # to know the max profit at step i, we only need to know the max profit at the previous two steps
    prev_max = 0
    curr_max = 0

    for i in range(len(nums)):
        curr = max(prev_max + nums[i], curr_max)
        prev_max = curr_max
        curr_max = curr

    return curr_max


test = [2, 7, 9, 3, 1]
print(rob(test), rob_efficient(test))
