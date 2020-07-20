def subsets_iterative(nums):
    """
    Iteratively update
    Time: O(n * 2^n)
    Space: O(1) res not included
    """
    res = [[]]
    for num in nums:
        # for every new number, create a copy of the current res,
        # and append num to every list in the copy
        res += [curr + [num] for curr in res]
    return res


def subsets(nums):
    """
    Backtracking
    Time: O(n * 2^n) 2^n, number of subsets of nums (each element can either be in or out of a subset)
    n, the time to copy the solution to res
    Space: O(n) the recursion stack and curr_res (res not included)
    """
    res = []

    def backtrack(start, curr_res):
        # unlike combination, where we append only when we are at the bottom layer
        # for subsets we append each node in the recursion tree (we can guarantee there are no repetitions)
        # make a copy of curr_res since we will pop its last element upon return to the previous layer
        res.append(curr_res[:])
        for i in range(start, len(nums)):
            curr_res.append(nums[i])
            # this search guarantees we won't have any repetition
            backtrack(i + 1, curr_res)
            # pop out so that the next element can join (same level)
            curr_res.pop()

    backtrack(0, [])
    return res


test = [1, 2, 4]
print(subsets_iterative(test))
