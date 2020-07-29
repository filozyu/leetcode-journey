def isSubsequence(s, t):
    """
    Two pointers
    Time: O(T) T - the length of t
    Space: O(1)
    """
    i, j = 0, 0

    while i < len(s):
        if j >= len(t):
            return False
        elif s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return True


test_s, test_t = "abc", "ahbgdc"
print(isSubsequence(test_s, test_t))
