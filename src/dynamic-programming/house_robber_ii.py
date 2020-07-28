def rob(nums):
    """
    Dynamic programming with two starting points
    Time: O(n)
    Space: O(1)
    """
    if len(nums) == 0:
        return 0

    # if the first house has been robbed
    first_curr_val = nums[0]
    first_prev_val = nums[0]

    # if the first house has not been robbed, equivalent to rob linear houses from 1 to n
    curr_val = 0
    prev_val = 0

    for i in range(1, len(nums)):

        # if the first house hsa not been robbed, the house to be robbed will start from i = 1
        # the last house can be robbed
        curr = max(curr_val, prev_val + nums[i])
        prev_val = curr_val
        curr_val = curr

        if 2 <= i < len(nums) - 1:
            # if the first house has been robbed,
            # the next house to rob is the third house (i = 2) and the last house cannot be robbed
            first_curr = max(first_curr_val, first_prev_val + nums[i])
            first_prev_val = first_curr_val
            first_curr_val = first_curr

    return max(first_curr_val, curr_val)


test = [2, 3, 2]
print(rob(test))
