def checkValidString(s):
    stack = []
    star_list = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            if len(stack) > 0:
                stack.pop()
            elif len(star_list) > 0:
                star_list.pop()
            else:
                return False
        else:
            star_list.append(i)
    while len(star_list) > 0 and len(stack) > 0:
        if star_list[-1] > stack[-1]:
            star_list.pop()
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

test = "(*()"
print(checkValidString(test))