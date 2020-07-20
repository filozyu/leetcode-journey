def permute(nums):
    """
    Backtracking
    Time: O(n * n!) for each appending, there will be n checking (?)
    Space: O(n) storage for curr_res and recursion stack (res not included)
    """
    res = []

    def backtrack(nums, curr_res):
        if len(curr_res) == len(nums):
            res.append(curr_res[:])
            return
        for num in nums:
            # the if condition checking will take O(n)
            if num not in curr_res:
                curr_res.append(num)
                # in every recursive call, scan every number in num,
                # unlike combination: cannot scan only later elements: e.g. [2] -> [2, 1]
                backtrack(nums, curr_res)
                curr_res.pop()

    backtrack(nums, [])

    return res


test = [1, 2, 3, 4]
print(permute(test))
