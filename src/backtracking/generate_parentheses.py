def generateParenthesis(n):
    if n == 1:
        return ["()"]
    prev_paren = generateParenthesis(n - 1)
    res = set()
    for candidate in prev_paren:
        res.add(candidate + "()")
        for i in range(len(candidate)):
            res.add(candidate[:i] + "(" + candidate[i:] + ")")
            for j in range(i + 1, len(candidate)):
                res.add(candidate[:i] + "(" + candidate[i:j] + ")" + candidate[j:])
    return list(res)


def generateParenthesis_recursion(n):
    res = set()

    def backtrack(s, left, right):
        if len(s) == n * 2:
            res.add(s)
        else:
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

    backtrack("", 0, 0)
    return res


# print(generateParenthesis(5))
print(generateParenthesis_recursion(3))
