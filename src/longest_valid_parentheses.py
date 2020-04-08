def longestValidParentheses(s):
    """
    Brute force
    Time: n^2 + (n-1)^2 + ... + 1 so O(n^3)
    Space: O(n) stack for checking valid parentheses
    """
    # helper function to check valid parentheses
    def check_valid(parentheses):
        stack = []
        for i in parentheses:
            if i == "(":
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                stack.pop()
        if stack:
            return False
        else:
            return True

    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i + 2, n + 1):
            if (j - i) % 2 == 0 and check_valid(s[i:j]):
                if j - i > max_len:
                    max_len = j - i
    return max_len


def longestValidParentheses_stack(s):
    """
    Stack of indices
    Time: O(n)
    Space: O(n)
    """
    len_s = len(s)
    # initialise stack
    # choosing -1 since if all are matching, then the correct length would be i - 0 + 1
    # i: index of the last matching ")"; 0: initial index
    stack = [-1]
    max_len = 0
    for i in range(len_s):
        # if the current char is "(", record the position
        if s[i] == "(":
            stack.append(i)
        # if the current char is ")", pop the last position out
        # if ")" is extra, the stack will be empty after popping
        # and the index of the this extra ")" will be pushed into the stack
        # when calculating the length, the result is 0
        else:
            stack.pop()
            # if stack is empty, which means the initial -1 has been popped out
            # therefore the number of ")" is 1 + number of "("
            # so does not form any valid parentheses
            if len(stack) == 0:
                # add the position of ")" to stack and new length will start counting from that position
                stack.append(i)
            # the last element in the stack is the position of the last unmatched "("
            # OR the new start point given by an invalid ")"
            max_len = max(max_len, i - stack[-1])
    return max_len

# test = ")()())"
# test = "()((()()()"
test = "(()"

print(longestValidParentheses_stack(test))
