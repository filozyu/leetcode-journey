def combinationSum3(k, n):
    """
    Backtracking
    Time: O(10 choose k), but after pruning the recursion tree should be smaller
    Space: O(k) curr_res and recursion stack
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []

    def backtrack(start, curr_res, curr_sum):
        # check the length and sum to exit the recursion
        if len(curr_res) == k and curr_sum == n:
            res.append(curr_res[:])
            return
        for i in range(start, len(nums)):
            if curr_sum + nums[i] > n:
                break
            curr_res.append(nums[i])
            # go from i + 1 to avoid repetition
            backtrack(i + 1, curr_res, curr_sum + nums[i])
            curr_res.pop()

    backtrack(0, [], 0)
    return res


test_k, test_n = 3, 9
print(combinationSum3(test_k, test_n))
