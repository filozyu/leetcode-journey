# dictionary, two pointers over two arrays
def intersect(nums1, nums2):
    """
    Dictionary
    Time: O(m+h) generate count_dict and loop through nums2; m, n = len(nums1), len(nums2)
    Space: O(m) count_dict, for nums1
    NOTE: here if we construct the count_dict for the smaller one between nums1 and nums2, the space is O(min(m,n))
    """
    res = []
    count_dict = {}
    for i in range(len(nums1)):
        if count_dict.get(nums1[i]) is not None:
            count_dict[nums1[i]] += 1
        else:
            count_dict[nums1[i]] = 1
    for j in range(len(nums2)):
        if count_dict.get(nums2[j]) is not None:
            # if encounter a number in num1
            if count_dict[nums2[j]] >= 1:
                # append to result
                res.append(nums2[j])
                # decrement the count
                count_dict[nums2[j]] -= 1
    return res


def intersect_sort(nums1, nums2):
    """
    Sorted case
    Time: O(mlogm + nlogn) if not sorted or O(m+n) if sorted
    Space: O(1)
    """
    res = []
    p1, p2 = 0, 0
    nums1.sort()
    nums2.sort()

    while p1 < len(nums1) and p2 < len(nums2):
        curr1, curr2 = nums1[p1], nums2[p2]
        if curr1 == curr2:
            res.append(curr1)
            p1 += 1
            p2 += 1
        elif curr1 > curr2:
            p2 += 1
        else:
            p1 += 1
    return res


test_1 = [1, 2, 2, 1]
test_2 = [2, 2]
print(intersect_sort(test_1, test_2))
