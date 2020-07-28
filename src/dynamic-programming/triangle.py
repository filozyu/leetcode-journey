def minimumTotal_recursion(triangle):
    """
    Recursion (Top down)
    Time: O(2^n) number of nodes in a full binary tree depth n
    Space: O(n) recursion stack
    """

    def recursive_by_layer(row, col):
        if row == len(triangle):
            # if we have reached the bottom, there is no more level beneath it
            return 0
        return (
            min(recursive_by_layer(row + 1, col), recursive_by_layer(row + 1, col + 1))
            + triangle[row][col]
        )

    return recursive_by_layer(0, 0)


def minimumTotal_recursion_memo(triangle):
    """
    Recursion with memory
    Time: O(n^2) we only need to calculate for each node once
    Space: O(n^2) storage for memo
    """
    memo = [["n/a"] * len(triangle) for _ in range(len(triangle))]

    def recursive_memo(row, col):
        if row == len(triangle):
            # if we have reached the bottom, there is no more level beneath it
            return 0
        if memo[row][col] == "n/a":
            memo[row][col] = (
                min(recursive_memo(row + 1, col), recursive_memo(row + 1, col + 1))
                + triangle[row][col]
            )

        return memo[row][col]

    return recursive_memo(0, 0)


def minimumTotal(triangle):
    """
    Dynamic programming
    Time: O(n^2) n is the number of rows in the triangle
    Space: O(n^2) for the 2D array
    """
    if len(triangle) > 0:
        if len(triangle[0]) > 0:
            # dp[i][j] stores the minimum path sum that ends at the j-th element in the i-th row
            dp = [[0] * len(triangle) for _ in range(len(triangle))]
            dp[0][0] = triangle[0][0]

            for i in range(1, len(triangle)):
                for j in range(len(triangle[i])):
                    if j == 0:
                        # edge case: left edge
                        dp[i][j] = dp[i - 1][j] + triangle[i][j]

                    elif j == len(triangle[i]) - 1:
                        # edge case: right edge
                        dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

                    else:
                        # state transfer
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

            return min(dp[-1])


def minimumTotal_efficient(triangle):
    """
    Dynamic programming with optimised storage
    Time: O(n^2) n is the number of rows in the triangle
    Space: O(n) since we only store two rows
    """
    if len(triangle) > 0:
        if len(triangle[0]) > 0:
            # dp[0 or 1][j] stores the minimum path sum that ends at the j-th element in the recent two rows
            dp = [[0] * len(triangle) for _ in range(2)]
            dp[0][0] = triangle[0][0]

            for i in range(1, len(triangle)):
                for j in range(len(triangle[i])):
                    # determine which row in dp are we updating
                    curr = i % 2
                    prev = 1 - curr
                    if j == 0:
                        # edge case: left edge
                        dp[curr][j] = dp[prev][j] + triangle[i][j]

                    elif j == len(triangle[i]) - 1:
                        # edge case: right edge
                        dp[curr][j] = dp[prev][j - 1] + triangle[i][j]

                    else:
                        # state transfer
                        dp[curr][j] = min(dp[prev][j - 1], dp[prev][j]) + triangle[i][j]

            return min(dp[(len(triangle) + 1) % 2])


test = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(
    minimumTotal_recursion(test),
    minimumTotal_recursion_memo(test),
    minimumTotal(test),
    minimumTotal_efficient(test),
)
