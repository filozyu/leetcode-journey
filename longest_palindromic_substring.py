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


def longestPalindrome_expand(s: str) -> str:
    """
    Expansion around centre (accepted, faster than dp)
    Time: O(n^2)
    Space: O(1)
    """
    if len(s) == 0:
        return ""
    max_len = 1
    max_idx = (0, 0)
    # loop for each centre, each expansion will take O(n), O(2n) expansions in total (odd and even)
    for i in range(0, len(s) - 1):
        # expansion for palindrome with odd length
        odd_span = expand(s, i, i)
        # expansion for palindrome with even length
        even_span = expand(s, i, i + 1)
        # Comparison
        if odd_span[1] - odd_span[0] + 1 > max_len:
            max_len = odd_span[1] - odd_span[0] + 1
            max_idx = (odd_span[0], odd_span[1])
        if even_span[1] - even_span[0] + 1 > max_len:
            max_len = even_span[1] - even_span[0] + 1
            max_idx = (even_span[0], even_span[1])

    return s[max_idx[0] : max_idx[1] + 1]


def expand(s, c_left, c_right):
    i, j = c_left, c_right
    while i >= 0 and j < len(s) and s[i] == s[j]:
        # expand if criterion is met
        i -= 1
        j += 1
    # after broken from the while loop, one extra expansion was done and need to be undone
    return i + 1, j - 1


test_inputs = ["aa", "cbbd", "aabbaa", "cadaca", "cadacca", "cafbacca"]
print([longestPalindrome_expand(test) for test in test_inputs])
