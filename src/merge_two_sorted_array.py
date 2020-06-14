# merge sort, two pointers
def merge(nums1, m, nums2, n):
    """
    Merge and sort
    Time: O((m+n)log(m+n))
    Space: O(1) no extra space
    """
    # note that we have to modify nums1 by changing nums1[:]
    # otherwise if we call nums1 directly, then a nums1 will be a new reference to whatever is assigned to it
    nums1[:] = sorted(nums1[:m] + nums2)


def merge_two_pointers_copy(nums1, m, nums2, n):
    """
    Two pointers with an extra copy
    Time: O(m+n)
    Space: O(m) the copy of nums1[:m]
    """
    nums1_copy = nums1[:m]
    nums1[:] = []
    # two pointers to scan through nums1 and nums2
    p_1, p_2 = 0, 0
    while p_1 < m and p_2 < n:
        # append the smaller to nums1
        if nums1_copy[p_1] <= nums2[p_2]:
            nums1.append(nums1_copy[p_1])
            p_1 += 1
        else:
            nums1.append(nums2[p_2])
            p_2 += 1
    # at the end, append all elements in whichever array is left
    if p_1 == m:
        nums1 += nums2[p_2:]
    elif p_2 == n:
        nums1 += nums1_copy[p_1:]


def merge_two_pointers_inplace(nums1, m, nums2, n):
    """
    Two pointers with no extra space
    Time: O(m+n)
    Space: O(1)
    """
    # nums1_fill is the indicator in nums1, telling us which element to feed now
    nums1_fill = len(nums1) - 1
    # p_1 and p_2 start from the rear of nums1 and nums2
    p_1, p_2 = m - 1, n - 1
    # loop before either reaches the head
    while p_1 >= 0 and p_2 >= 0:
        # in this case put nums1[p_1] to the current element to be filled
        if nums1[p_1] >= nums2[p_2]:
            nums1[nums1_fill] = nums1[p_1]
            # move pointer for nums1 towards the head
            p_1 -= 1
        # in this case put nums2[p_2] to the current element to be filled
        else:
            nums1[nums1_fill] = nums2[p_2]
            # move pointer for nums2 towards the head
            p_2 -= 1
        # move to the next element to be filled
        nums1_fill -= 1
    # put the rest of nums2 at the head of nums1
    if p_1 == -1:
        nums1[:p_2 + 1] = nums2[:p_2 + 1]


test_1 = [1, 2, 3, 0, 0, 0]
test_m = 3
test_2 = [2, 5, 6]
test_n = 3

merge_two_pointers_inplace(test_1, test_m, test_2, test_n)
print(test_1)
