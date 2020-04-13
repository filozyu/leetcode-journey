def findMaxLength(nums):
    """
    Brute force
    Time: O(n^2)
    Space: O(1)
    Check for every possible subarray whether it is valid or not, record the length if valid
    """
    n = len(nums)
    max_len = 0
    for i in range(n):
        curr_sum = nums[i]
        for j in range(i + 1, n):
            curr_sum += nums[j]
            if (j - i + 1) % 2 == 0 and curr_sum == (j - i + 1) / 2:
                max_len = max(j - i + 1, max_len)
    return max_len


def findMaxLength_hash(nums):
    """
    One pass hash map
    Time: O(n)
    Space: O(n)
    Idea behind is that whenever the same count at two indices A and B are recorded
    the subarray [A+1, B] inclusive has equal numbers of zeroes and ones
    """
    # initialise count_dict with 0, of position -1, so that whenever count goes back to 0 again
    # we know that the subarray starting from the first number till the current index is valid
    count_dict = {0: -1}
    count = 0
    max_len = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1
        # CAUTION: cannot use if count_dict.get(count) directly
        # since if count is a key and the corresponding value is 0, then this evaluates to False
        # to verify is a key is in a dict, use dict.get(key) is not None instead
        if count_dict.get(count) is not None:
            max_len = max(i - count_dict[count], max_len)
        else:
            count_dict[count] = i
    return max_len


def findMaxLength_dp(nums):
    # DOES NOT WORK, is it possible to make it work by just using a 1-D DP array and how?
    # dp[i] records the max length of the subarray ends at index i
    # This method fails to work with test = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
    # in particular, it fails to recognise dp[9] should be 8 rather than 0

    length = len(nums)
    max_len = 0
    dp = [0] * length
    for i in range(1, length):
        if nums[i] != nums[i - 1]:
            if i == 1:
                dp[i] = 2
            else:
                dp[i] = dp[i - 2] + 2
        elif i - dp[i - 1] - 1 < 0:
            continue
        elif nums[i] != nums[i - dp[i - 1] - 1]:
            if i - dp[i - 1] - 1 == 0:
                dp[i] = dp[i - 1] + 2
            else:
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        else:
            continue

        max_len = max(max_len, dp[i])
    print(dp)
    return max_len


# test = [
# 1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,0,
# 1,1,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,1
# ]
# test = [1,1,1,1,0,0,0,0,0,1,1,0]
# test = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0]
test = [0, 0, 1]
print(findMaxLength_hash(test))
