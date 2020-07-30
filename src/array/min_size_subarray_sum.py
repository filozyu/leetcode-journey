# Sliding window
def minSubArrayLen_slowest(s, nums):
    """
    Brute force (Time limit exceeded)
    Time: O(n^3) (n^2 to loop over all subarray and n to sum) the dominating term is sum of k^2, k = 1,...,n
    Space: O(1)
    """
    length = len(nums)
    min_len = length + 1
    for i in range(length):
        for j in range(i, length):
            if sum(nums[i:j+1]) >= s:
                min_len = min(min_len, j - i + 1)
                # break here since we don't need to check larger j's, which are bound to be >= s but longer
                break
    if min_len == length + 1:
        return 0
    else:
        return min_len


def minSubArrayLen_slow(s, nums):
    """
    Brute force (with a maintained sum)
    Time: O(n^2)
    Space: O(n) the space for sums
    """
    length = len(nums)
    if length == 0:
        return 0
    min_len = length + 1
    sums = [0] * length
    sums[0] = nums[0]

    # sums[i] stores the cumulative sum of nums up to index i
    for i in range(1, length):
        sums[i] = sums[i - 1] + nums[i]

    for i in range(length):
        for j in range(i, length):
            # the sum of the subarray can be calculated using the cumulative sum
            curr_sum = sums[j] - sums[i] + nums[i]
            if curr_sum >= s:
                min_len = min(min_len, j - i + 1)
                # break here since we don't need to check larger j's, which are bound to be >= s but longer
                break

    if min_len == length + 1:
        return 0
    else:
        return min_len


def minSubArrayLen(s, nums):
    """
    Sliding window
    Time: O(n)
    Space: O(1)
    """
    length = len(nums)
    if length == 0:
        return length
    # both ends of the sliding window
    w_l, w_r = 0, 0
    min_len = length + 1
    # the initial window contains only nums[0]
    curr_sum = nums[0]
    # loop until the right hand side of the window has reached the end
    # or iterate the right pointer from 0 to length - 1 in a for loop,
    # and advance the left pointer in a while loop if the condition is met
    while w_r < length:
        # if the condition is satisfied, move the left side towards the right to find shorter window
        if curr_sum >= s:
            min_len = min(min_len, w_r - w_l + 1)
            # if we can still move the left side
            if w_l < length - 1:
                # update the sum
                curr_sum -= nums[w_l]
                w_l += 1
            # if we cannot move the left side, we have finished traversing the array
            else:
                break
        # if the condition is not met, move the right side towards the right to include more numbers
        else:
            # if we can still move the right side
            if w_r < length - 1:
                # update the sum
                w_r += 1
                curr_sum += nums[w_r]
            # if we cannot move the right side, we have finished traversing the array
            else:
                break

    if min_len == length + 1:
        return 0
    else:
        return min_len


test_s = 7
test = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(test_s, test))
