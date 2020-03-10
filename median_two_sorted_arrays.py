def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
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


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
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


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums2)
    n = len(nums1)
    if (n + m) % 2 == 0:
        left = int((n + m) / 2)
        right = int((n + m) / 2) + 1
        return (find_k_smallest(nums1, 0, nums2, 0, left) + \
                find_k_smallest(nums1, 0, nums2, 0, right)) / 2
    else:
        return find_k_smallest(nums1, 0, nums2, 0, int((n + m) / 2))

def find_k_smallest(nums1, start1, nums2, start2, k):
    if k == 1:
        return min(nums1[start1], nums2[start2])
    # len1 = end1 - start1 + 1
    # len2 = end2 - start2 + 1
    len1 = len(nums1) - start1 - 1
    len2 = len(nums2) - start2 - 1

    if len1 == 0:
        return nums2[start2 + k - 1]
    elif len2 == 0:
        return nums1[start1 + k - 1]

    nums1_stop = start1 + min(len1, int(k / 2)) - 1
    nums2_stop = start2 + min(len2, int(k / 2)) - 1
    # nums1_stop = min(start1 + int(k/2), len1) - 1
    # nums2_stop = min(start2 + int(k/2), len2) - 1

    if nums1[nums1_stop] < nums2[nums2_stop]:
        next_k = k - (nums1_stop - start1 + 1)
        start1 = nums1_stop + 1

    else:
        next_k = k - (nums2_stop - start2 + 1)
        start2 = nums2_stop + 1

    return find_k_smallest(nums1, start1, nums2, start2, next_k)




