def numIslands(grid):
    """
    Depth First Search (on graph)
    Time: O(m*n), m length of grid and n width of grid
    Space: O(m*n), worst, when every element in grid is "1"
    """
    def dfs(root, grid):
        grid_len = len(grid)
        grid_wid = len(grid[0])
        stack = [root]
        while len(stack) > 0:
            node_i, node_j = stack.pop()
            # set visited nodes to zero
            grid[node_i][node_j] = "0"

            # up
            if node_i > 0 and grid[node_i - 1][node_j] == "1":
                stack.append((node_i - 1, node_j))
            # left
            if node_j > 0 and grid[node_i][node_j - 1] == "1":
                stack.append((node_i, node_j - 1))
            # down
            if node_i < grid_len - 1 and grid[node_i + 1][node_j] == "1":
                stack.append((node_i + 1, node_j))
            # right
            if node_j < grid_wid - 1 and grid[node_i][node_j + 1] == "1":
                stack.append((node_i, node_j + 1))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                dfs((i, j), grid)
                count += 1
    return count


test = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
print(numIslands(test))
