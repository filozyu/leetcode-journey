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


def moveZeroes_two_pointers_1(nums):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    """
    non_zero_next = 0
    n = len(nums)
    for i in range(n):
        # for every number if it is not zero, swap it with the last nonzero's next element
        # if non_zero_next == i: equivalent to no swapping at all since nums[i] != 0
        if nums[i] != 0:
            nums[non_zero_next], nums[i] = nums[i], nums[non_zero_next]
            # after swapping the last nonzero advances 1, so is non_zero_next
            non_zero_next += 1


def moveZeroes_two_pointers_2(nums):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    """
    last_non_zero = 0
    n = len(nums)
    for i in range(n):
        # last_non_zero records the index of the last seen non-zero number
        if nums[i] != 0 and i > last_non_zero:
            # assign the non-zero number to the next of last_non_zero
            nums[last_non_zero + 1] = nums[i]
            # swap if the next of last_non_zero is not i
            if last_non_zero + 1 != i:
                nums[i] = 0
            # update last_non_zero
            last_non_zero += 1


test = [0, 1, 0, 3, 12]
moveZeroes_two_pointers_2(test)
print(test)
