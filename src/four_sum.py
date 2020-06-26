# Hash set, two pointers (colliding)
def fourSum(nums, target):
    """
    Dict of pairs
    Time: above O(n^2) (depends on pair_1 and pair_2)
    Space: O(n^2)
    """
    res = set()
    sum_dict = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            curr_sum = nums[i] + nums[j]
            if sum_dict.get(curr_sum) is not None:
                sum_dict[curr_sum].append([i, j])
            else:
                sum_dict[curr_sum] = [[i, j]]
            if sum_dict.get(target - curr_sum) is not None:
                for pair_1 in sum_dict[target - curr_sum]:
                    for pair_2 in sum_dict[curr_sum]:
                        inds = list(set(pair_1).union(set(pair_2)))
                        if len(inds) == 4:
                            potential_sol = tuple(sorted([nums[i] for i in inds]))
                            res.add(potential_sol)
    return res


def fourSum_two_pointers(nums, target):
    """
    Two pointers
    Time: O(n^3)
    Space: O(1)
    """
    res = []
    nums.sort()
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
    return res


test = [-3, -2, -1, 0, 0, 1, 2, 3]
tar = 0

test_2 = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
tar_2 = -9

print(fourSum_two_pointers(test_2, tar_2))
