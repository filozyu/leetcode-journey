from utils import binary_search, binary_search_left, binary_search_right


def searchRange(nums, target):
    """
    Binary search (INCORRECT)
    Time: ?? worst case O(n): e.g. find 2 in [2,2,2,2,2,2], best case O(logn)
    Space: O(1) (no copies of input created)
    """
    n = len(nums)

    curr_ind = binary_search(nums, target, 0, n - 1)
    if curr_ind == -1:
        return -1, -1
    left_ind, right_ind = curr_ind, curr_ind

    if left_ind != 0:
        while nums[left_ind - 1] == nums[left_ind]:
            left_ind = binary_search(nums, target, 0, left_ind - 1)
            if left_ind == 0:
                break
    first_occur = left_ind
    if right_ind != n - 1:
        while nums[right_ind + 1] == nums[right_ind]:
            right_ind = binary_search(nums, target, right_ind + 1, n - 1)
            if right_ind == n - 1:
                break
    last_occur = right_ind
    return first_occur, last_occur


def searchRange_binary(nums, target):
    """
    Binary search (twice, one for the first occurrence, one for the last)
    Time: O(logn)
    Space: O(1)
    """
    return binary_search_left(nums, target), binary_search_right(nums, target)


test = [3, 3, 3, 3, 3, 3, 4]
print(searchRange_binary(test, 3))
