# DFS, flood fill
def numDistinctIslands(grid):
    """
    Depth First Search then translate all islands to the top left corner
    Time: O(m*n), m length of grid and n width of grid
    Space: O(m*n)
    """
    # up, left, down, right
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    def in_grid(row_id, col_id):
        """
        Check if row_id and col_id is valid in the grid
        """
        assert len(grid) >= 1 and len(grid[0]) >= 1
        if 0 <= row_id <= len(grid) - 1 and 0 <= col_id <= len(grid[0]) - 1:
            return True
        else:
            return False

    def dfs(root):
        stack = [root]
        shape = set()

        translate_i, translate_j = root[0], root[1]
        # Note: calculating the translation from the root to (0, 0)
        # will probably lead to some nodes in the island being out of the grid after translation
        # but that does not matter since if two islands are of the same shape,
        # then the DFS is bound to discover the same node in both islands (regarding to shape, not positions in grid)
        # so the same node (shape-wise) will be translated to (0, 0),
        # and all the other nodes will be translated to the same (possibly negative) coordinates around (0, 0)
        # e.g. (1) 1 1  and  (1) 1 1  has the same (1) in the shape, although they are in different position in grid
        #          1             1

        while len(stack) > 0:
            node_i, node_j = stack.pop()
            shape.add((node_i - translate_i, node_j - translate_j))
            # set visited nodes to zero
            grid[node_i][node_j] = 0

            for direction in directions:
                next_i, next_j = node_i + direction[0], node_j + direction[1]
                if in_grid(next_i, next_j) and grid[next_i][next_j] == 1:
                    stack.append((next_i, next_j))

        # creating a frozenset from a set could take O(n) where n is the length of the set
        shapes.add(frozenset(shape))

    shapes = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                dfs((i, j))
    return len(shapes)


test = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
print(numDistinctIslands(test))
