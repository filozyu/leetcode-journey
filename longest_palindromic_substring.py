def longestPalindrome(s: str) -> str:
    """
    Brute force (time limit exceeded)
    Time: O( /sum_{i=0}^{i=n-1}(n-i+1)(n-i) ) >= O(n^2) or crudely O(n^3) if each check on palindrome will take O(n)
    Space: O(n)
    """
    if len(s) == 0:
        return ""
    max_len = 1
    max_str = s[0]
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            med = int((i + j) / 2)
            curr_str = s[i:j]
            if (j - i) % 2 == 0:
                # slicing list will take (j-i)/2 * 3, one for slicing s, two for slicing and reversing s
                if s[i:med] == s[med:j][::-1]:
                    if len(curr_str) > max_len:
                        max_len = len(curr_str)
                        max_str = curr_str
            elif s[i:med] == s[med + 1 : j][::-1]:
                if len(curr_str) > max_len:
                    max_len = len(curr_str)
                    max_str = curr_str
    return max_str


def longestPalindrome_dp(s: str) -> str:
    """
    Dynamic programming (accepted, but slow)
    (will have time limit exceeded error if use np.array instead of built-in list)
    Time: O(n^2)
    Space: O(n^2)
    """
    if len(s) == 0:
        return ""
    max_len = 1
    max_idx = (0, 0)
    # dp[i][j] is True if s[i:j+1] is a palindrome and False otherwise
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    # i loops backward
    for j in range(0, len(s)):
        # j loops forward starting from i (so that dp is expanding)
        # Alternatively j loops forward and i loops backward from j
        # for i in range(len(s) - 1, -1, -1):
        #    for j in range(i, len(s)):
        for i in range(j, -1, -1):
            # base case
            if j - i <= 2:
                if s[i] == s[j]:
                    dp[i][j] = 1
            else:
                # s[i : j+1] is palindrome if s[i+1 : j] is palindrome and s[i] is the same as s[j]
                dp[i][j] = dp[i + 1][j - 1] * int(s[i] == s[j])
            if dp[i][j] == 1 and max_len < (j - i + 1):
                max_len = j - i + 1
                max_idx = (i, j)
    return s[max_idx[0] : max_idx[1] + 1]


test_input = "abacbca"
print(longestPalindrome_dp(test_input))
