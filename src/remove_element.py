def removeElement(nums, val):
    """
    Swap deletions and non-deletion elements
    Time: O(n)
    Space: O(1)
    """
    # First find the first occurrence of val
    del_pos = -1
    for i in range(len(nums)):
        if nums[i] == val:
            del_pos = i
            break
    # If val has not occurred, return the original list
    if del_pos == -1:
        return len(nums), nums

    # otherwise swap the element to be deleted with a nearest non-deletion element
    for i in range(len(nums)):
        if nums[i] != val and i > del_pos:
            nums[del_pos], nums[i] = nums[i], nums[del_pos]
            # there are two possibilities after swapping:
            # 1. i == del_pos + 1, so now nums[i] == val and we can move del_pos to be i
            # 2. i > del_pos + 1, that means nums[del_pos + 1] == val, and we need to delete del_pos + 1 as well
            del_pos += 1
    return del_pos, nums[:del_pos]


def removeElement_plain(nums, val):
    """
    One pass
    Time: O(n)
    Space: O(1)
    """
    non_del_pos = 0
    # after each round, we are sure that,
    # all numbers up till nums[i] that need NOT to be deleted are kept in nums[:non_del_pos]
    for i in range(len(nums)):
        if nums[i] != val:
            if non_del_pos != i:
                nums[non_del_pos] = nums[i]
            non_del_pos += 1
    return non_del_pos, nums[:non_del_pos]


def removeElement_tail(nums, val):
    """
    Copy the tail
    The number of assignments (or copies) is the same as the number of elements to be deleted
    EFFICIENT WHEN THERE ARE ONLY FEW ELEMENTS NEED TO BE DELETED
    Time: O(n)
    Space: O(1)
    """
    dup_pos = 0
    tail_pos = len(nums) - 1
    # note: the if statement below has to be <= since otherwise the loop won't be run if dup_pos == tail_pos
    # consider e.g. nums = [1], val = 1. Then dup_pos = tail_pos = 0
    while dup_pos <= tail_pos:
        # if the current element is to be removed, copy the last element in nums and to the current number
        # we can do this since there is no requirement of maintaining the order of the original nums
        # and since we have copied the value of the last element,
        # we can safely delete it (by curtailing the length by 1)
        # NOTE: it is possible that nums[tail_pos] is also val and therefore needs to be deleted,
        # but we don't have to worry about this, since we will check nums[dup_pos] next time, until it is no longer val
        if nums[dup_pos] == val:
            nums[dup_pos] = nums[tail_pos]
            tail_pos -= 1
        # now that nums[dup_pos] != val, we don't need to copy anything, simply move forward
        else:
            dup_pos += 1
    # upon return, dup_pos == tail_pos + 1
    # all remained elements (no need for deletion) are now in nums[:dup_pos]
    return dup_pos, nums[:dup_pos]


test = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
print(removeElement(test, val))
print(removeElement_plain(test, val))
print(removeElement_tail(test, val))
