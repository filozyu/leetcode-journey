def combine_slow(n, k):
    """
    (Time Limit Exceeded)
    Time: O(n^k + (n choose k) * klogk), n^k for recursion and we will add to res (n choose k) times, with sorting
    Space: O(k) the recursion stack and curr_res (res not included)
    """
    res = set()

    def backtrack(candidates, curr_res):
        if len(curr_res) == k:
            # appending to the result will be O(klogk)
            res.add(tuple(sorted(curr_res)))
            return
        # the following loop will run for n in every recursive call, there will be k layers in the recursion tree
        # that is every node will have n children and the tree has a depth of k
        # the total time complexity is therefore n^k
        for next_num in candidates:
            if next_num in curr_res:
                continue
            else:
                curr_res.add(next_num)
                backtrack(candidates, curr_res)
                curr_res -= {next_num}

    backtrack(set(range(1, n + 1)), set())

    return res


def combine(n, k):
    """
    Time: O((n choose k) * k) since after finding a combination, we slice and copy it into res
    Space: O(k) the recursion stack and curr_res (res not included)
    """
    res = []

    def backtrack(start, curr_res):
        if len(curr_res) == k:
            # copy (by slicing) time will be O(k)
            # if we do not create a copy here, the pop() in the next loop will affect the lists added to res
            res.append(curr_res[:])
            return
        for i in range(start, n + 1):
            curr_res.append(i)
            # only look for numbers after i, therefore the combinations never repeat themselves
            # e.g. 4 choose 2: [1,] -> [1, 2] ->pop(2)-> [1, 3] ->pop(3)-> [1, 4] ->pop(4)-> [1,] ->pop(1)-> [2,] ...
            backtrack(i + 1, curr_res)
            # reset the appended curr_res to append in the next iteration (at this level)
            curr_res.pop()

    backtrack(1, [])

    return res


test_n, test_k = 4, 2
print(combine(test_n, test_k))
