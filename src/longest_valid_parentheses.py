def longestValidParentheses_slow(s):
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


def longestValidParentheses_dp(s):
    """
    Dynamic programming
    Time: O(n)
    Space: O(n) storage for dp
    dp[i] is the max length of parentheses ending at the i-th char in s
    so dp is zero for all the positions of "("
    """
    length = len(s)
    max_len = 0
    dp = [0] * length
    for i in range(1, length):
        # case 1: ....()
        if s[i] == ")" and s[i - 1] == "(":
            # if i > 2, get the previous length of parentheses
            if i > 2:
                dp[i] = dp[i - 2] + 2
            else:
                dp[i] = 2
        # case 2: ....))
        # the last two conditions:
        # 1) s[i - dp[i-1]] should be a "(", to match the ")" at s[i-1]; note that dp[i-1] <= i
        # so if i-dp[i-1] == 0: then i+1 must be odd and therefore no match
        # 2) the char before the "(" we located in 1) must also be a "(" to match with s[i]
        elif (
            s[i] == ")"
            and s[i - 1] == ")"
            and i - dp[i - 1] >= 1
            and s[i - dp[i - 1] - 1] == "("
        ):
            # dp[i - dp[i - 1] - 2] here in case there are any consecutive parentheses separated by s[i - dp[i - 1] - 1]
            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        max_len = max(max_len, dp[i])
    return max_len


def longestValidParentheses_two_pointers(s):
    """
    Two pointers
    Time: O(n)
    Space: O(1)
    two passes (from start to end and from end to start)
    left records number of "("
    right records number of ")"
    """
    max_len = 0
    length = len(s)
    # first pass: cannot detect say (()()
    # but can detect ()())
    left, right = 0, 0
    for i in range(length):
        # reset left and right if invalid
        if right > left:
            left, right = 0, 0
        if s[i] == "(":
            left += 1
        else:
            right += 1
        # calculate the length every time when the parentheses are matching
        if right == left:
            max_len = max(max_len, right + left)

    # second pass: cannot detect say ()())
    # but can detect (()()
    left, right = 0, 0
    for i in range(length - 1, -1, -1):
        # reset left and right if invalid
        if right < left:
            left, right = 0, 0
        if s[i] == "(":
            left += 1
        else:
            right += 1
        # calculate the length every time when the parentheses are matching
        if right == left:
            max_len = max(max_len, right + left)

    return max_len


# test = ")()())"
# test = "()((()()()"
# test = "(()"
# test = "(()))())("
test = "()()"

print(longestValidParentheses_two_pointers(test))
