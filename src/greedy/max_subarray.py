def maxSubArray(nums):
    """
    Brute force (Time Limit Exceeded)
    Time: O(n)
    Space: O(1)
    """
    n = len(nums)
    max_val = nums[0]
    for i in range(n):
        for j in range(i + 1, n + 1):
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


def maxSubArray_divide_conquer(nums):
    """
    Divide and conquer
    Time: O(nlogn) recursion will be called logn times and in every call, O(n) for getting the cross_max
    Space: O(logn) depth of recursion stack
    """
    n = len(nums)
    if n == 1:
        # base case
        return nums[0]
    median = n // 2
    left = nums[:median]
    right = nums[median:]
    left_max = maxSubArray_divide_conquer(left)
    right_max = maxSubArray_divide_conquer(right)

    # Compute the cross_max, it has to be an subarray crossing the centre points
    # computed by adding the left part (all the way to the start)
    # and the right part (all the way to the end) from the centre
    # The subarray is sprang from the two centre points
    # since these two points have to be in the optimal subarray that crosses left and right
    # if the sum does not increase, the loop will carry on to both ends, but the sum does not increase
    centre_left = nums[median - 1]
    curr_sum_left = 0
    # left part of the cross subarray
    for i in range(median - 1, -1, -1):
        curr_sum_left += nums[i]
        centre_left = max(curr_sum_left, centre_left)

    centre_right = nums[median]
    curr_sum_right = 0
    # right part of the cross subarray
    for i in range(median, n):
        curr_sum_right += nums[i]
        centre_right = max(curr_sum_right, centre_right)

    cross_max = centre_left + centre_right
    # return the max of left, right and cross
    return max(left_max, right_max, cross_max)


test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray_divide_conquer(test))
