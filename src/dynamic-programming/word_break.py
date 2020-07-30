from collections import deque


def wordBreak_recursion(s, wordDict):
    """
    Plain recursion (Time Limit Exceeded)
    Time: O(n^n) or O(2^n) ? worst case: s = "aaaab" wordDict = ["a", "aa", "aaa", "aaaa"]
    Space: O(n) depth of recursion stack
    """
    if s in wordDict:
        return True
    for i in range(len(s)):
        curr_substr = s[:i]
        if curr_substr in wordDict:
            if wordBreak_recursion(s[i:], wordDict):
                return True
    return False


def wordBreak_recursion_memo(s, wordDict):
    """
    Recursion with memory (Time Limit Exceeded)
    Time: O(n^2) ??
    Space: O(n) depth of recursion stack and memo
    """

    def recur_memo(s, wordDict, memo):
        if not memo.get(s):
            if s in wordDict:
                memo[s] = True
                return memo[s]

            for i in range(len(s)):
                if s[:i] in wordDict and recur_memo(s[i:], wordDict, memo):
                    memo[s[:i]] = True
                    memo[s] = True
                    return memo[s]
            memo[s] = False
        return memo[s]

    memo = {}

    return recur_memo(s, wordDict, memo)


def wordBreak_BFS(s, wordDict):
    """
    BFS
    Time: O(n^2) (for every character, loop till the end)
    Space: O(n) queue and visited
    """
    wordDictSet = set(wordDict)
    queue = deque()
    # visited serves as memory, since we might visit the same starting index multiple times
    visited = [0] * len(s)
    # start index (root)
    queue.append(0)

    while queue:
        # for start's children, i.e. all substrings starting from start
        start = queue.popleft()
        # if we have already visited start without returning,
        # that means none of the sub-trees under start form a solution
        # if we have not visited start:
        if visited[start] == 0:
            # loop through all possible substring,
            # but only those that can be found in the dict are actual children of start
            for end in range(start + 1, len(s) + 1):
                # only append the index to tree if the substring between start and end can be found
                if s[start:end] in wordDictSet:
                    queue.append(end)
                    # in this case, no more further substrings
                    # and all previous substrings can be matched
                    # return True
                    if end == len(s):
                        return True
            # mark start as visited
            visited[start] = 1
    # when the queue is empty, we still don't have a match, return False
    return False


def wordBreak_DP(s, wordDict):
    """
    Dynamic programming
    Time: O(n^2)
    Space: O(n) the dp list
    """
    wordDictSet = set(wordDict)
    # dp[i] = True if s[:i] can be represented in wordDict
    # all dp are initialised as False
    dp = [0] * (len(s) + 1)
    dp[0] = True
    # get the current substring, indexed by i
    for i in range(1, len(s) + 1):
        # divide substring into two smaller substrings, from beginning to j and from j to i
        for j in range(0, i):
            # check for all possible split of the current substring
            # if the first substring is true and so is the second substring,
            # the whole substring from beginning to i is true
            # break the j for loop and start for the next i
            if dp[j] and s[j:i] in wordDictSet:
                dp[i] = True
                break

    return dp[len(s)]


test_s = "goalspecial"
test_d = ["go", "goal", "goals", "special"]
print(wordBreak_DP(test_s, test_d))
