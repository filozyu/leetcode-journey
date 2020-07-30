def moveZeroes(nums):
    """
    Time: O(n^2) (worst case: [0, 0, 0, 0, ..., 1])
    Space: O(1)
    """
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == 0:
            # pop i will take O(n-i)
            nums.pop(i)
            nums.append(0)
            n -= 1
        else:
            i += 1


def moveZeroes_linear(nums):
    """
    Two passes
    Time: O(n)
    Space: O(n)
    """
    non_zero_nums = []
    # put all non-zero elements in nums
    for i in range(len(nums)):
        if nums[i] != 0:
            non_zero_nums.append(nums[i])
    # copy non_zero_nums to nums and set the rest of nums to zeros
    for i in range(len(nums)):
        if i < len(non_zero_nums):
            nums[i] = non_zero_nums[i]
        else:
            nums[i] = 0

    return nums


def moveZeroes_two_pointers(nums):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    """
    non_zero_next = 0
    n = len(nums)
    for i in range(n):
        # for every number if it is not zero, swap it with the last nonzero's next element (non_zero_next)
        # then update non_zero_next
        if nums[i] != 0:
            # to prevent swapping the same element when non_zero_next == i
            if non_zero_next != i:
                nums[non_zero_next], nums[i] = nums[i], nums[non_zero_next]
            # after swapping the last non-zero advances 1, so non_zero_next also advances 1
            non_zero_next += 1


test = [0, 1, 0, 3, 12]
moveZeroes_two_pointers(test)
print(test)
