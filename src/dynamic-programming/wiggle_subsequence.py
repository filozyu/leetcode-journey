def wiggleMaxLength(nums):
    """
    Dynamic programming
    Time: O(n^2) n - length of nums
    Space: O(n) for dp
    """
    if len(nums) == 0:
        return 0

    # dp[i][0] holds the longest wiggle subsequence ending with nums[i],
    # and nums[i] > the previous number in the subsequence
    # so the next number to be added should < nums[i]

    # dp[i][1] holds the longest wiggle subsequence ending with nums[i],
    # and nums[i] < the previous number in the subsequence
    # so the next number to be added should > nums[i]

    dp = [[0, 0] for _ in range(len(nums))]

    # initialise
    dp[0] = [1, 1]
    max_len = 1

    for i in range(len(nums)):
        for j in range(0, i):

            if nums[j] > nums[i]:
                # nums[i] is smaller than the last in sequence (nums[j])
                dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                if dp[i][1] > max_len:
                    max_len = dp[i][1]

            elif nums[i] > nums[j]:
                # nums[i] is greater than the last in sequence (nums[j])
                dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                if dp[i][0] > max_len:
                    max_len = dp[i][0]

    return max_len


def wiggleMaxLength_fast(nums):
    """
    Dynamic programming with optimised space
    Time: O(n)
    Space: O(n)
    """

    if len(nums) == 0:
        return 0

    # up[i] stores the max length of the subsequence from nums[0], ..., nums[i]
    # with the last number greater than the penultimate number
    up = [0] * len(nums)

    # down[i] stores the max length of the subsequence from nums[0], ..., nums[i]
    # with the last number less than the penultimate number
    down = [0] * len(nums)

    for i in range(len(nums)):
        if i == 0:
            up[i] = 1
            down[i] = 1

        # if the current number < the previous number
        # then we update down
        elif nums[i] < nums[i - 1]:
            # if nums[i-1] is the ending number of the optimal subseq in up[i-1]
            # and suppose down[i] >= up[i-1] + 2, then we can find a subseq with up ending number
            # from nums[0], ..., nums[i-1] with length at least up[i-1] + 1 != up[i-1]

            # if nums[i-1] is not the ending number of the optimal subseq in up[i-1],
            # assume the ending number is x, then there are two possibilities:
            # 1) nums[i-1] >= x: in this case nums[i-1] can serve as the end of the subseq as well
            # 2) nums[i-1] < x: in this case nums[i] < x, if down[i] > up[i-1] + 1 (cannot be less)
            # then down[i] must be at least up[i-1] + 2, which means after removing the last number,
            # the resulting suseq will end with an up and has length up[i-1] + 1 != up[i-1], contradiction

            down[i] = up[i-1] + 1
            up[i] = up[i-1]

        # if the current number > the previous number
        # then we update up
        elif nums[i] > nums[i - 1]:
            up[i] = down[i-1] + 1
            down[i] = down[i-1]

        # if the current number = the previous number
        # then we do not update
        else:
            up[i] = up[i-1]
            down[i] = down[i - 1]

    return max(up[len(nums) - 1], down[len(nums) - 1])


test = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
print(wiggleMaxLength_fast(test))
