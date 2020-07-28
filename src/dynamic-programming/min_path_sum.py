def minPathSum(grid):
    """
    Dynamic Programming
    Time: O(m * n) m rows n columns
    Space: O(m * n)
    """
    if len(grid) > 0:
        rows = len(grid)
        if len(grid[0]) > 0:
            cols = len(grid[0])

            dp = [[0] * cols for _ in range(rows)]
            dp[0][0] = grid[0][0]

            for i in range(0, rows):
                for j in range(0, cols):

                    if i == 0 and j == 0:
                        continue

                    elif i == 0:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]

                    elif j == 0:
                        dp[i][j] = dp[i - 1][j] + grid[i][j]

                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

            return dp[rows - 1][cols - 1]


def minPathSum_in_place(grid):
    """
    Dynamic programming in-place
    Time: O(m * n)
    Space: O(1)
    """
    if len(grid) > 0:
        rows = len(grid)
        if len(grid[0]) > 0:
            cols = len(grid[0])
            for i in range(rows):
                for j in range(cols):
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        grid[i][j] = grid[i][j - 1] + grid[i][j]
                    elif j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

            return grid[rows - 1][cols - 1]


test = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(test), minPathSum_in_place(test))
