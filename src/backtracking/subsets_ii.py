def subsetsWithDup_slow(nums):
    """
    Backtracking
    Time: O(klogk * 2^n) k - the average length of a subset, n - length of nums
    Space: O(k) recursion stack and curr_res (res not included)
    """
    res = set()

    def backtrack(start, curr_res):
        res.add(tuple(sorted(curr_res)))
        for i in range(start, len(nums)):
            curr_res.append(nums[i])
            backtrack(i + 1, curr_res)
            curr_res.pop()

    backtrack(0, [])

    return res


def subsetsWithDup(nums):
    """
    Backtracking with pruning
    Time: O(k * 2^n) k - the average length of a subset, n - length of nums
    Space: O(k) recursion stack and curr_res (res not included)
    """
    res = []
    # sort first, to help detect duplicates
    nums.sort()

    def backtrack(start, curr_res):
        res.append(curr_res[:])
        for i in range(start, len(nums)):
            # if we have found duplicates (in the same level) skip it
            # since all the subsets developed from nums[i] have already been stored in step i - 1
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr_res.append(nums[i])
            backtrack(i + 1, curr_res)
            curr_res.pop()

    backtrack(0, [])

    return res


test = [4, 4, 4, 1, 4]
print(subsetsWithDup(test))
