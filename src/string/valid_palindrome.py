# colliding two pointers
def isPalindrome(s):
    """
    Colliding two pointers
    Time: O(n)
    Space: O(1)
    """
    start, end = 0, len(s) - 1
    while start < end:
        # c.isalnum() returns False if c is neither a letter nor a number
        if not s[start].isalnum():
            start += 1
            continue
        if not s[end].isalnum():
            end -= 1
            continue
        if s[start].lower() != s[end].lower():
            return False
        else:
            start += 1
            end -= 1
    return True


test = "A man, a plan, a canal: Panama"
print(isPalindrome(test))
