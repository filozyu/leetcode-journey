# two pointers (colliding)
import math


def threeSumClosest(nums, target):
    """
    Brute force
    Time: O(n^3)
    Space: O(1)
    """
    closest = math.inf
    if len(nums) <= 3:
        return sum(nums)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                curr_sum = nums[i] + nums[j] + nums[k]
                if math.fabs(target - curr_sum) < math.fabs(target - closest):
                    closest = curr_sum
    return closest


def threeSumClosest_two_pointers(nums, target):
    """
    Two pointers in sorted nums
    Time: O(n^2)
    Space: O(1) or O(logn) if counting the space for sorting
    """
    res_sum = 0
    if len(nums) <= 3:
        return sum(nums)
    diff = math.inf
    nums.sort()
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            curr_diff = abs(curr_sum - target)
            if curr_diff == 0:
                return curr_sum
            if curr_diff < diff:
                diff = curr_diff
                res_sum = curr_sum
            if curr_sum > target:
                right -= 1
            elif curr_sum < target:
                left += 1

    return res_sum


test = [-1, 2, 1, -4]
tar = 1
print(threeSumClosest_two_pointers(test, tar))
