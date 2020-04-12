def search(nums, target):
    """
    Binary Search
    Time: O(logn)
    Space: O(1)
    """
    n = len(nums)
    left, right = 0, n - 1
    # eliminate trivial cases
    if n == 0 or nums[0] > target > nums[-1]:
        return -1

    while left <= right:
        mid = (right + left) // 2
        # found target
        if target == nums[mid]:
            return mid
        # if target greater than the middle one:
        # Three possibilities
        # 1. The middle one is after the rotation point and target is greater than the first one (search left)
        # 2. The middle one is after the rotation point and target is smaller than the last one (search right)
        # 3. The middle one is before the rotation point and target is greater than the first one (search right)
        elif target > nums[mid]:
            # 1
            if target >= nums[0] > nums[mid]:
                right = mid - 1
            # 2 & 3
            else:
                left = mid + 1
        # if target smaller than the middle one:
        # Three possibilities
        # 1. The middle one is before the rotation point and target is smaller than the last one (search right)
        # 2. The middle one is before the rotation point and target is greater than the first one (search left)
        # 3. The middle one is after the rotation point and target is smaller than the last one (search left)
        else:
            # 1
            if target <= nums[-1] < nums[mid]:
                left = mid + 1
            # 2 & 3
            else:
                right = mid - 1
    # if outside the while loop, target not found
    return -1


def binary_search(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        median = (right + left) // 2
        if target == nums[median]:
            return median
        elif target > nums[median]:
            left = median + 1
        else:
            right = median - 1

    return -1


test = [5, 7, 9, 12, 1, 3]
test_tar = 3
print(search(test, test_tar))
