# Find K numbers in nums such that their sum equals to target


def KSum(nums, target, K):
    """
    K sum by two pointers
    Time: O(n^(K-1))
    Space: O(K) for the recursion stack
    """
    nums.sort()
    results = []
    find_KSum(nums, 0, len(nums) - 1, target, K, [], results)
    return results


def find_KSum(nums, left, right, target, k, result, results):
    """
    Recursive calculate k sum
    :param nums: the sorted nums
    :param left: the index in nums to start the search (inclusive)
    :param right: the index in nums to end the search (inclusive)
    :param target: the target to be found
    :param k: number of elements in nums to sum
    :param result: the result to the current k sum problem
    :param results: the results for the over all K sum problem
    :return: None, results are recorded in result and results
    """
    if (
        right - left + 1 < k
        or k < 2
        or target < nums[left] * k
        or target > nums[right] * k
    ):  # early termination
        return
    if k == 2:  # two pointers solve sorted 2-sum problem
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                results.append(result + [nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif s < target:
                left += 1
            else:
                right -= 1
    else:  # recursively reduce k
        for i in range(left, right + 1):
            if i == left or (i > left and nums[i - 1] != nums[i]):
                find_KSum(
                    nums,
                    i + 1,
                    right,
                    target - nums[i],
                    k - 1,
                    result + [nums[i]],
                    results,
                )
