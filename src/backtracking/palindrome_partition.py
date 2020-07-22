def is_palindrome(s):
    """
    Check palindrome
    one pass, time: O(len(s))
    """
    if s == "" or s == []:
        return False
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


def partition(s):
    """
    Backtracking
    Time: O(n * 2^n) worst case if s is "aaaaaaa...", then there will be 2^n set of partitions, each with n char
    Space: O(n) curr_res and recursion stack (res not considered)
    """
    res = []

    def backtrack(start, curr_res):
        if start == len(s):
            res.append(curr_res[:])
            return

        for i in range(start, len(s)):
            if is_palindrome(s[start: i + 1]):
                curr_res.append(s[start: i + 1])
                backtrack(i + 1, curr_res)
                curr_res.pop()

    backtrack(0, [])

    return res


test = "aab"
print(partition(test))
