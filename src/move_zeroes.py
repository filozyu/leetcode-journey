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


# def moveZeroes_two_pointers(nums):
#     """
#     Two pointers
#     Time:
#     Space:
#     """




