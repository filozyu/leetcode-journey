def reverseString(s):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseString_recursion(s):
    """
    Recursion with two pointers (just an extra and frankly not necessary step)
    Time: O(n)
    Space: O(n) size of the recursion stack
    """

    def recur(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            recur(left + 1, right - 1)

    recur(0, len(s) - 1)


test = ["a", "b", "c", "d", "e"]
reverseString_recursion(test)
print(test)
