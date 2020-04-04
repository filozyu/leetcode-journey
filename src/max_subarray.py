def maxSubArray(nums):
    """
    Brute force (Time Limit Exceeded)
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    max_val = nums[0]
    for i in range(n):
        for j in range(i+1, n+1):
            curr_sum = sum(nums[i:j])
            if curr_sum > max_val:
                max_val = curr_sum
    return max_val


def maxSubArray_greedy(nums):
    """
    Greedy (similar to dynamic programming, but with smaller memory)
    Time: O(n)
    Space: O(1)
    """
    # Greedy algo makes locally optimal choice at each stage
    # this leads to the overall optimal choice
    n = len(nums)
    max_val, curr_max = nums[0], nums[0]
    for i in range(1, n):
        # curr_max at index i records the running max sum that involves nums[i]
        # nums[i] can either be counted in an existing subarray or as the start of a new subarray
        curr_max = max(nums[i], curr_max + nums[i])
        # max_val at index i records the max sum in the array nums[0:i+1] (i+1 elements)
        max_val = max(max_val, curr_max)
    # return the last max_val, which is the max sum in the array nums[0:n+1] (nums)
    return max_val


# test = [-2,1,-3,4,-1,2,1,-5,4]
test = [2,-5]
print(maxSubArray_greedy(test))
