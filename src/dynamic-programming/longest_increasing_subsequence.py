def lengthOfLIS(nums):
    """
    Dynamic programming
    Time: O(n^2) n - length of nums
    Space: O(n)
    """
    # dp[i] contains the max length of increasing subsequence ending with i
    dp = [1] * len(nums)
    curr_max = 0

    for i in range(len(nums)):
        for j in range(0, i):
            # for all the previous increasing subsequences,
            # find those that nums[j] can append to, then get the max length
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

        # update the overall maximum across nums
        if dp[i] > curr_max:
            curr_max = dp[i]

    return curr_max


test = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(test))
