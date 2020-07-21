from collections import defaultdict


def combinationSum2(candidates, target):
    """
    Backtracking
    Time: ?
    Space: O(k) k the average length of combination
    """
    res = set()
    # sort the candidates first to reduce time in forming a combination (pruning the recursion tree)
    candidates.sort()

    def backtrack(start, curr_res, curr_sum):
        if curr_sum == target:
            # since res only contains unique combinations
            # time here: O(klogk)
            res.add(tuple(sorted(curr_res)))
            return

        for i in range(start, len(candidates)):

            if curr_sum + candidates[i] > target:
                # stop exploring further with solutions containing the remaining numbers in candidates,
                # since all the possible extensions from the remaining numbers will be greater than target
                break

            if i > start and candidates[i] == candidates[i - 1]:
                # always consider the fist occurrence (candidates[i - 1]),
                # but since in the same loop,
                # we have considered all the possible extensions of candidates[i - 1] in step i - 1,
                # all the extensions of candidates[i] are already considered in the previous step (i - 1) as well
                continue

            curr_res.append(candidates[i])
            backtrack(i + 1, curr_res, curr_sum + candidates[i])
            curr_res.pop()

    backtrack(0, [], 0)

    return res


def combinationSum2_DP(candidates, target):
    """
    Bottom-up DP
    Time: ?
    Space: ?
    """
    candidates.sort()
    dp = defaultdict(set)
    # add an empty combination to start with
    dp[0].add(())

    for num in candidates:
        # search in [num, target] inclusive on both ends
        # loop backward to avoid using the same element more than once
        # we have to update larger number first, otherwise
        # e.g. when num = 1
        # 1: [1] -> 2: [1, 1] -> 3: [1, 1, 1]
        for t in range(target, num - 1, -1):
            # update dp[t]
            for prev in dp[t - num]:
                # t - num would be a number in [0, target - num]
                # after each iteration, dp[t] contains combinations of nums with sum t
                # (num,) is a tuple contains only num
                dp[t].add(prev + (num,))
    return dp[target]


test = [10, 1, 2, 7, 6, 1, 5]
test_target = 8

test_2 = [1, 1]
test_target_2 = 2
print(combinationSum2_DP(test, test_target))
print(combinationSum2_DP(test_2, test_target_2))
