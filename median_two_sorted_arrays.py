from typing import List


def findMedianSortedArrays_one(nums1: List[int], nums2: List[int]) -> float:
    """
    Brute force

    Time: O((m+n)*log(m+n))
    Space: O(m+n)
    """
    # actually very fast since sorted by built-in method
    comb = sorted(nums1 + nums2)
    length = len(comb)
    if length % 2 == 0:
        return (comb[int(length / 2)] + comb[int(length / 2) - 1]) / 2
    else:
        return comb[int(length / 2)]


def findMedianSortedArrays_two(nums1: List[int], nums2: List[int]) -> float:
    """
    Merge sort

    Time: O(m+n) (worst case, the last step of merge sort)
    Space: O(m+n)
    """
    comb = []
    i, j = 0, 0
    while len(comb) < len(nums1) + len(nums2):
        if i == len(nums1):
            comb += nums2[j:]
            break
        if j == len(nums2):
            comb += nums1[i:]
            break
        if nums1[i] < nums2[j]:
            comb.append(nums1[i])
            i += 1
        else:
            comb.append(nums2[j])
            j += 1
    length = len(comb)
    if length % 2 == 0:
        return (comb[int(length / 2)] + comb[int(length / 2) - 1]) / 2
    else:
        return comb[int(length / 2)]


def findMedianSortedArrays_three(nums1, nums2):
    """
    Binary search
    Time: O(log(m+n))
    Space: O(1)
    """

    m = len(nums2)
    n = len(nums1)
    if (n + m) % 2 == 0:
        left = int((n + m) / 2)
        right = int((n + m) / 2) + 1
        return (find_k_smallest(nums1, 0, nums2, 0, left) + \
                find_k_smallest(nums1, 0, nums2, 0, right)) / 2
    else:
        return find_k_smallest(nums1, 0, nums2, 0, int((n + m) / 2) + 1)


def find_k_smallest(nums1, start1, nums2, start2, k):

    # suppose A[k/2] < B[k/2] then A[0],...,A[k/2] < B[k/2]
    # also B[0],...,B[k/2 - 1] < B[k/2], suppose B[0],...,B[k/2 - 1] < A[k/2] as well
    # then the number of elements smaller than A[k/2] (at most): k/2 - 1 + k/2 - 1 = k - 2
    # if B[0],...,B[k/2 - 1] < A[k/2] is not true, then the above number (k-2) can only decrease
    # thus moving further away from the median
    # anyway A[k/2] is at most the (k-1)th smallest number in the combined array
    # so we can safely delete all the numbers before and include A[k/2] in A

    len1 = len(nums1) - start1
    len2 = len(nums2) - start2

    # if one of the arrays reaches its end, return immediately
    if len1 == 0:
        return nums2[start2 + k - 1]
    elif len2 == 0:
        return nums1[start1 + k - 1]

    # if none of the arrays reach the end, and k is reduced to 1
    if k == 1:
        return min(nums1[start1], nums2[start2])

    # the new sub-arrays of (combined) length k to be checked
    nums1_stop = start1 + min(len1, int(k / 2)) - 1
    nums2_stop = start2 + min(len2, int(k / 2)) - 1

    # every call will reduce the search space by k/2, so
    # (m+n)/2 -> (m+n)/4 -> (m+n)/8 -> (m+n)/16 -> ...
    # stop until k = 1 (or prematurely if one of the arrays reaches its end)
    # therefore number of calls: log(m+n)
    if nums1[nums1_stop] < nums2[nums2_stop]:
        next_k = k - (nums1_stop - start1 + 1)
        start1 = nums1_stop + 1

    else:
        next_k = k - (nums2_stop - start2 + 1)
        start2 = nums2_stop + 1

    return find_k_smallest(nums1, start1, nums2, start2, next_k)
