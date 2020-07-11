def evalRPN(tokens):
    """
    Stack, pop two operands then append back the result
    NOTE: all numbers are integer and divisions are rounded towards zero (not floor division)
    Time: O(n) one pass of the tokens
    Space: O(n) stack
    """
    stack = []
    for i in range(len(tokens)):
        if tokens[i] in "+-*/":
            right = stack.pop()
            left = stack.pop()
            if tokens[i] == "+":
                stack.append(left + right)
            elif tokens[i] == "-":
                stack.append(left - right)
            elif tokens[i] == "*":
                stack.append(left * right)
            else:
                stack.append(int(left / right))
        else:
            stack.append(int(tokens[i]))
    return stack.pop()


test = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(test))
