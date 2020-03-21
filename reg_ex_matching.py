import re
#TODO: UNFINISHED
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

#TODO: Add and understand DP solution

s = "abc"
p = "a*c"
# p = "ab*a*c*.*"
# s = "aaaccc"
# p = "a*c*ccc"
try:
    correct = re.match(p, s)[0] == s
except:
    correct = False

print(
    "String: {}\n".format(s),
    "Pattern: {}\n".format(p),
    "Result: {}\n".format(isMatch_recurrsion_memo(s, p)),
    "Correct: {}".format(correct),
    sep="",
)
