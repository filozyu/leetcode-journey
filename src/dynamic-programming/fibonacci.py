def climbStairs_recursive(n):
    """
    Recursion
    Time: O(2^n) number of nodes in the recursion tree
    Space: O(n) recursion stack (depth of the recursion tree)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2

    return climbStairs_recursive(n - 1) + climbStairs_recursive(n - 2)


def climbStairs_recursive_memo(n):
    """
    Recursion with memo (top down)
    Time: O(n) number of nodes in the recursion tree has now been reduced to order n
    Space: O(n) recursion stack and memo
    """
    memo = [0] * (n + 1)

    def climb(n, memo):
        if n == 1:
            memo[n] = 1
        elif n == 2:
            memo[n] = 2

        elif memo[n] == 0:
            memo[n] = climb(n - 1, memo) + climb(n - 2, memo)

        return memo[n]

    return climb(n, memo)


def climbStairs_dp(n):
    """
    Dynamic programming (bottom up)
    Time: O(n) number of iterations
    Space: O(n) storage of climbing
    """
    climbing = [0] * (n + 1)
    climbing[1] = 1
    climbing[2] = 2
    for i in range(3, n + 1):
        climbing[i] = climbing[i - 1] + climbing[i - 2]

    return climbing[n]


def climbStairs_iterative(n):
    """
    Iteration
    Time: O(n)
    Space: O(1)
    """
    if n == 1:
        return 1
    first = 1
    second = 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third

    return second


test = 2
print(
    climbStairs_recursive(test),
    climbStairs_recursive_memo(test),
    climbStairs_dp(test),
    climbStairs_iterative(test),
)
