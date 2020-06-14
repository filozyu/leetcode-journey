# colliding two pointers
def twoSum(numbers, target):
    """
    Colliding two pointers (since numbers is sorted)
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            # return indices start from 1
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
    # results not found
    return [0, 0]


test = [2, 7, 11, 15]
tar = 9
print(twoSum(test, tar))
