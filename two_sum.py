# Q1
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# One pass hash table
# Time: O(n)
# Space: O(n)


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_ind_dict = {}
    for i in range(len(nums)):
        # check before adding to the dict can prevent conflicting keys
        # e.g. nums = [3. 3], target = 6
        if target - nums[i] in num_ind_dict:
            return [num_ind_dict[target - nums[i]], i]
        else:
            num_ind_dict[nums[i]] = i
