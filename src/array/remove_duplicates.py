# Two pointers
def removeDuplicates(nums):
    """
    Two pointers (non_repeat_len and i)
    Modify the input in-place, where the sole concern are the unique values, which should be placed at the front
    Time: O(n)
    Space: O(1)
    """
    # non_repeat_len indicates the number of unique elements we have so far,
    # and nums[:non_repeat_len] is free of duplicates
    non_repeat_len = 1
    for i in range(1, len(nums)):
        # if we have found a new element (for the first time)
        # alternatively the if statement can be replaced by:
        # if nums[i] != nums[non_repeat_len - 1] (a new unique value at i)
        if nums[i] != nums[i - 1]:
            # assign it to the next element in nums[:non_repeat_len], i.e. nums[non_repeat_len]
            nums[non_repeat_len] = nums[i]
            # increment non_repeat_len since now nums[:non_repeat_len + 1] is free of duplicates
            non_repeat_len += 1
    return non_repeat_len, nums[:non_repeat_len]


test = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(test))
