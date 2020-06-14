# Two pointers
def removeDuplicates(nums):
    """
    Two pointers, with many conditions
    Time: O(n)
    Space: O(n)
    """
    # the slow pointer: stop_ind
    stop_ind = 0  # [0, stop_ind] contains the results
    count = 1  # number of (consecutive, since the list is sorted) occurrence of nums[stop_ind] in [0, stop_ind]

    for i in range(len(nums)):
        # check if index is valid
        if stop_ind + 1 >= len(nums):
            break

        # the following condition is True for two cases:
        # 1) nums[stop_ind - 1] and nums[stop_ind] are the same, but nums[i] is not, update
        # in 1), nums[stop_ind + 1] is the same as nums[stop_ind] and needs to be overwritten by nums[i]
        # 2) nums[stop_ind - 1], nums[stop_ind] and nums[i] are all the same, do not update
        # in 2), nums[stop_ind + 1] is less than nums[stop_ind] (since the latter has been overwritten)
        if nums[i] > nums[stop_ind + 1] and count == 2:
            if not nums[i] == nums[stop_ind]:
                nums[stop_ind + 1] = nums[i]
                count = 1
                stop_ind += 1

        # if the following condition is True, we will overwrite nums[stop_ind + 1]
        elif nums[i] > nums[stop_ind + 1] and count < 2:
            nums[stop_ind + 1] = nums[i]
            # the following condition is True then we are still updating the same pair
            if nums[stop_ind + 1] == nums[stop_ind]:
                count += 1
            # otherwise, it means we are starting with a new pair
            else:
                count = 1
            stop_ind += 1

        # this part is only reached if nums[i] == nums[stop_ind + 1]
        # if the following statement is True, then no overwriting is needed
        elif nums[stop_ind + 1] > nums[stop_ind]:
            count = 1
            stop_ind += 1

        # if the following statement is True, then we are in the same pair, no need for overwriting
        elif nums[stop_ind + 1] == nums[stop_ind] and count < 2:
            count += 1
            stop_ind += 1

        # if the following statement is True, then we need to overwrite nums[stop_ind + 1]
        elif nums[stop_ind + 1] == nums[stop_ind] and count == 2:
            continue

    return stop_ind + 1, nums[:stop_ind + 1]


def removeDuplicates_pop(nums):
    """
    Popping
    Time: O(n^2) worst case: all numbers in nums are the same
    Space: O(1)
    """
    count = 1
    i = 1
    while True:
        # stop the loop
        if i >= len(nums):
            break

        # still in a pair
        if nums[i] == nums[i - 1] and count < 2:
            count += 1
            i += 1

        # duplicate detected, remove
        elif nums[i] == nums[i - 1] and count == 2:
            # pop time complexity: O(n)
            nums.pop(i)

        # start a new pair
        elif nums[i] > nums[i - 1]:
            count = 1
            i += 1

    return len(nums), nums


def removeDuplicates_two_pointers(nums):
    """
    Another way of two pointers
    Time: O(n)
    Space: O(n)
    """
    stop_ind_next = 1  # here stop_ind_next indicates the next element of the processed array
    count = 1  # count has to start from 1 since we are starting with nums[0]
    # i should start the loop at the same position as stop_ind_next
    for i in range(1, len(nums)):
        # now we have encountered more an element at stop_ind_next that needs to be removed
        if count >= 2:
            # the following statement will be True once i proceed to a different element than nums[stop_ind_next]
            # all nums[stop_ind_next] to nums[i] will be the same
            if nums[i] != nums[i - 1]:
                # copy (overwrite) nums[stop_ind_next] with the next different element
                nums[stop_ind_next] = nums[i]
                stop_ind_next += 1
                # count is now 1 again
                count = 1
        # we can add one more element that is the same as nums[stop_ind_next - 1]
        else:
            nums[stop_ind_next] = nums[i]
            # if nums[stop_ind_next] is not the same, reset count
            if nums[stop_ind_next] != nums[stop_ind_next - 1]:
                count = 1
            else:
                count += 1
            stop_ind_next += 1

    return stop_ind_next, nums[:stop_ind_next]


# test = [1, 2, 2]
# test = [1, 1, 1, 2, 2, 3]
# test = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# test = [1, 1, 1, 1, 1, 2, 2, 2, 4]
test = [0, 0, 1, 1, 1, 2, 3, 3, 3, 4, 4]
print(removeDuplicates_two_pointers(test))
