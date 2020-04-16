
def combinationSum(candidates, target):
    res_set = set()

    def backtrack(candidate, curr_sum, nums, tar):
        if curr_sum == target:
            res_set.add(tuple(sorted(candidate)))
            return
        elif curr_sum > target:
            return
        for c in nums:
            if curr_sum + c > tar:
                continue
            candidate.append(c)
            curr_sum += c
            backtrack(candidate, curr_sum, nums, tar)
            curr_sum -= candidate.pop()

    backtrack([], 0, candidates, target)

    return res_set


test_list = [2,3,5]
test_target = 8
print(combinationSum(test_list, test_target))
