def permuteUnique_slow(nums):
    """
    Backtracking
    Time: O(n * n!)
    Space: O(n) recursion stack and curr_res (res not included)
    """
    res = set()

    def backtrack(curr_res):
        # backtrack on indices rather than on elements
        if len(curr_res) == len(nums):
            # recover the elements from the indices
            # O(n)
            res.add(tuple(nums[i] for i in curr_res))
            return
        for i in range(len(nums)):
            # the if condition checking will take O(n)
            if i not in curr_res:
                curr_res.append(i)
                # in every recursive call, scan every number in from 0 to num - 1,
                backtrack(curr_res)
                curr_res.pop()

    backtrack([])

    return res


def permuteUnique(nums):
    """
    Backtracking with pruning
    Time: O(n * n!)
    Space: O(n) recursion stack and curr_res (res not included)
    """
    nums.sort()
    res = []
    used = [False] * len(nums)

    def backtrack(curr_res, used):
        # used[i] records whether the i-th element in nums has just been used in this combination (curr_res)
        if len(curr_res) == len(nums):
            res.append(curr_res[:])
            return
        for i in range(len(nums)):
            # only expand the solution if nums[i] has not been used in this combination
            if not used[i]:
                # no need to search further down the tree
                # if nums[i] is the same as the last one and the last one has not been used in this combination
                # e.g. nums = [1, 1, 2]
                # if we have already searched all combinations with position k being the first 1 (nums[0])
                # then all the combinations with position k being the second 1 (nums[1])
                # in the above case, when considering position k,
                # if nums[0] has not being used already in the first k-1 positions,
                # then we don't need to consider nums[1] since we have obtained all the combinations
                # from the last iteration also at the same level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # now include nums[i] in the current combination, set used[i] to True
                used[i] = True
                curr_res.append(nums[i])
                backtrack(curr_res, used)
                # undo the selection, remove nums[i] and set used[i] to False
                used[i] = False
                curr_res.pop()

    backtrack([], used)

    return res


test = [1, 1, 2]
print(permuteUnique(test))
