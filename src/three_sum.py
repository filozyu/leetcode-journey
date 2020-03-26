from collections import defaultdict

from utils import timer


def threeSum_slow(nums):
    """
    Brute force (time limit exceeded)
    Time: O(n^3)
    Space: O(m) m: unique number of triples that sum to zeros
    """
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    if sorted([nums[i], nums[j], nums[k]]) not in res:
                        res.append(sorted([nums[i], nums[j], nums[k]]))
    return res


def threeSum_hash(nums):
    """
    Hash tables (time limit exceeded)
    Time: between O(n^2) and O(n^3), depends on the k loop, in worst case, k loops for n times (e.g. [0, 0, 0, 0, 0])
    Space: O(m+n) m: unique number of triples that sum to zeros
    """
    res = []
    complement = defaultdict(list)
    for i in range(len(nums)):
        complement[-nums[i]].append(i)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if complement.get((nums[i] + nums[j])):
                for k in complement[(nums[i] + nums[j])]:
                    # make sure i, j themselves are not used to form a triplet
                    if k not in [i, j]:
                        # sorted to avoid add the same triplet to res
                        to_append = sorted([nums[i], nums[j], nums[k]])
                        if to_append not in res:
                            res.append(to_append)
    return res


def threeSum_two_pointers(nums):
    """
    Two pointers (fast)
    Time: O(n^2) (loop for the pointers of length n within every loop for i)
    Space: O(m) m: unique number of triples that sum to zeros, storage of results
    """
    nums = sorted(nums)
    res = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while right > left:
            s = nums[left] + nums[right] + nums[i]
            if s < 0:
                left += 1
                # no need to update if the next ele is the same
                # since this will not induce duplicate triplets to be appended to res
                # extra checks are slower than just doing another while loop
                # the same when s > 0
            elif s > 0:
                right -= 1
            else:
                # repetitiveness cannot be checked by an `IF (a,b,c) NOT IN res` statement
                # will have time limit exceeded error, instead, using the two while loops below
                res.append([nums[i], nums[left], nums[right]])
                # if match, left and right have to move otherwise sum would not be zero if only one's moving
                # i is still the same i
                left += 1
                right -= 1
                # keep on updating if the next ele is the same (both left and right)
                # since the list is sorted, all the same elements must be neighbouring
                # so doing this can avoid counting the same triplets more than once
                # Consider [-2, 0, 0, 2, 2]
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return res


# test = [0, 0, 0]
# test = [-1, 0, 1, 2, -1, -4]
# test = [-1, -1, 2]
test = [-2, 0, 2, 0, 2]
print(threeSum_two_pointers(test))
print("two pointer", timer(1, threeSum_two_pointers, test))
print("hash table", timer(1, threeSum_hash, test))
print("brute force", timer(1, threeSum_slow, test))
