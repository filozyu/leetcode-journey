# Two pointers on two arrays, set
def intersection(nums1, nums2):
    """
    Set intersection
    Time: O(m+n) converting lists to sets; m, n = len(nums1), len(nums2)
    Space: O(m+n) the two sets created
    """
    # OR
    # return list(set(nums1).intersection(set(nums2)))
    return list(set(nums1) & set(nums2))


def intersection_sorted(nums1, nums2):
    """
    Assume nums1 and nums2 are sorted, if not, sort them first
    Time: O(nlogn + mlogm) for sorting, if already sorted, then time O(m+n)
    Space: O(1) - result is not included
    """
    result = []
    # pointer p1 for nums1, p2 for nums2
    p1, p2 = 0, 0
    nums1.sort()
    nums2.sort()
    while p1 < len(nums1) and p2 < len(nums2):
        curr1, curr2 = nums1[p1], nums2[p2]
        if curr1 == curr2:
            result.append(curr1)
            # keep increment p1 as long as it's valid until we obtain a different value
            while p1 < len(nums1) and nums1[p1] == curr1:
                p1 += 1
            # keep increment p2 as long as it's valid until we obtain a different value
            while p2 < len(nums2) and nums2[p2] == curr2:
                p2 += 1
        # now only increment p1
        elif curr1 < curr2:
            while p1 < len(nums1) and nums1[p1] == curr1:
                p1 += 1
        # now only increment p2
        else:
            while p2 < len(nums2) and nums2[p2] == curr2:
                p2 += 1
    return result


test_1 = [1, 2, 2, 1]
test_2 = [2, 2]
print(intersection(test_1, test_2))
