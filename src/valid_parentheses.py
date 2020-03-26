def isValid(s):
    """
    Straight forward stack approach
    Time: O(n)
    Space: O(n)
    """
    match_dict = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = []
    for i in s:
        if stack and match_dict.get(i):
            if stack.pop() != match_dict[i]:
                return False
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True


# test = "([)]"
test = "(({()}){}[])"
print(isValid(test))
