import re
# DIFFICULT


def isMatch_recurrsion(s, p):
    """
    Recursion (slow, but accepted)
    Time: ??
    Space: not O(1) since the recursion will take up some spaces
    """
    # if no pattern to match and the string is empty, then matching is correct, otherwise incorrect
    if not p:
        return not s

    # if s and p matches for the first char, if not can either be the the second char in p is * or matching incorrect
    first_match = len(s) > 0 and (p[0] == s[0] or p[0] == ".")
    # if the second char in p is *
    if len(p) >= 2 and p[1] == "*":
        # two possibilities if the second char in p is *
        # 1) * stands for repetition >= 1, if first char matched then keep p unchanged (to keep *) and move s forward
        # 2) * stands for repetition = 0, then move on to the char after * in p, even the first char matched
        #    as in s="ccc" and p="c*ccc"
        return (first_match and isMatch_recurrsion(s[1:], p)) or isMatch_recurrsion(
            s, p[2:]
        )
    else:
        # if first char matched and the second char in p is not *, move both s and p forward
        return first_match and isMatch_recurrsion(s[1:], p[1:])


def isMatch_recurrsion_memo(s, p):
    """
    Recursion (fast, same as recursion, with memory)
    Time: ??
    Space: not O(1) since the recursion will take up some spaces
    """
    memo = dict()
    # memo can help avoid computing the same states in recursion, so is dp below

    def memo_update(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if j == len(p):
            return i == len(s)

        first_match = i < len(s) and (p[j] == s[i] or p[j] == ".")

        if j + 1 < len(p) and p[j + 1] == "*":
            ans = (first_match and memo_update(i + 1, j)) or memo_update(i, j + 2)
        else:
            ans = first_match and memo_update(i + 1, j + 1)
        memo[(i, j)] = ans
        return ans

    return memo_update(0, 0)


def isMatch_dp(s, p):
    """
    Dynamic programming, no recursive call presented
    Time: O(SP) (S, P = len(s), len(p))
    Space: O(SP) (dp)
    """

    # adding spaces to avoid indices go below zeros, as in the example p="c*a*b" and s="aab"
    s_new = " " + s
    p_new = " " + p

    # dp[i][j] is whether the first i characters in s_new can be matched by the first j characters in p_new
    # if s_new and p_new matched, so will s and p
    # i and j are number of characters! not indices
    dp = [[False for _ in range(len(p_new)+1)] for _ in range(len(s_new)+1)]

    # base case, only used to initialise dp[1][1], which is certainly True
    dp[0][0] = True

    # for the i-th char in s_new (the first space included)
    for i in range(1, len(s_new)+1):
        # for the j-th char in p_new (the first space included)
        for j in range(1, len(p_new)+1):
            # the i-th char in s_new is s_new[i-1], the j-th char in p_new is p_new[j-1[
            if s_new[i-1] == p_new[j-1] or p_new[j-1] == ".":
                dp[i][j] = dp[i-1][j-1]

            # otherwise if j-th char in p_new is *
            elif p_new[j-1] == "*":
                # if the j-1 -th char in p matches with the i-th char in s
                if s_new[i-1] == p_new[j-2] or p_new[j - 2] == ".":
                    # * could repeat: one or more times OR no repeat
                    dp[i][j] = dp[i - 1][j] or dp[i][j-2]
                    # alternatively (?) * could repeat: more than one time OR one time OR no repeat
                    # dp[i][j] = dp[i - 1][j] or dp[i][j-1] or dp[i][j-2]
                else:
                    # otherwise * can only repeat zero time
                    dp[i][j] = dp[i][j-2]

    return dp[-1][-1]

# s = "aab"
# p = "c*a*b"
# #
# s = "ab"
# p = ".*c"
s = "aa"
p = "a*"

# s = "aaaccc"
# p = "ab*a*c*.*"
# p = "a*c*ccc"

try:
    correct = re.match(p, s)[0] == s
except:
    correct = False

print(
    "String: {}\n".format(s),
    "Pattern: {}\n".format(p),
    "Result: {}\n".format(isMatch_dp(s, p)),
    "Correct: {}".format(correct),
    sep="",
)
