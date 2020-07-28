# dictionary
def isAnagram(s, t):
    """
    Time: O(m) m, n = len(s), len(t)
    Space: O(1) since ch_count is at most of size 26, when only considering the lower case letters
    """
    if len(s) != len(t):
        return False
    ch_count = {}
    # construct ch_count from s
    for i in range(len(s)):
        if ch_count.get(s[i]) is not None:
            ch_count[s[i]] += 1
        else:
            ch_count[s[i]] = 1
    # check t using ch_count
    for j in range(len(t)):
        # if there is no t[j] in s or that we have matched all of the previous such characters in s
        # not an anagram
        if ch_count.get(t[j]) is None or ch_count[t[j]] <= 0:
            return False
        # otherwise update ch_count to indicate we have matched one such character
        else:
            ch_count[t[j]] -= 1

    return True


test_s = "anagram"
test_t = "nagaram"
print(isAnagram(test_s, test_t))
