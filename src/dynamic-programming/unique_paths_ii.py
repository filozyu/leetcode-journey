def uniquePathsWithObstacles(obstacleGrid):
    """
    Dynamic programming
    Time: O(m * n)
    Space: O(m * n)
    """
    # if there is an obstacle at the starting position, no paths can be found
    if obstacleGrid[0][0] == 1:
        return 0
    rows = len(obstacleGrid)
    if rows > 0:
        cols = len(obstacleGrid[0])
        if cols > 0:
            dp = [[0] * cols for _ in range(rows)]

            dp[0][0] = 1

            for i in range(rows):
                for j in range(cols):
                    # do not update if there is an obstacle in the current position
                    # (default value is 0)
                    if (i == 0 and j == 0) or obstacleGrid[i][j] == 1:
                        continue
                    # otherwise update as usual
                    elif i == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif j == 0:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            return dp[rows - 1][cols - 1]


test = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(uniquePathsWithObstacles(test))
