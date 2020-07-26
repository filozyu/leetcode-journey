def pacificAtlantic(matrix):
    """
    DFS on pacific and atlantic, return the union
    Time: O(m * n) number of cells in the matrix
    Space: O(m * n) recursion stack, visited and the two lists to contain pacific and atlantic
    """

    def dfs(pos_x, pos_y, ocean):
        # DFS on a certain ocean
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        if ocean == "P":
            # any cell in the first row and the first column will be in the ocean
            edge_x, edge_y = 0, 0
            pacific.append((pos_x, pos_y))
        else:
            # any cell in the last row and the last column will be in the ocean
            edge_x, edge_y = rows - 1, cols - 1
            atlantic.append((pos_x, pos_y))
        # add to visited to prevent cycles
        visited.add((pos_x, pos_y))
        for d in directions:
            new_x = pos_x + d[0]
            new_y = pos_y + d[1]
            if (
                0 <= new_x < rows
                and 0 <= new_y < cols
                and (new_x, new_y) not in visited
            ):
                # if not visited and the new coordinates are legal
                if (
                    matrix[new_x][new_y] >= matrix[pos_x][pos_y]
                    or new_x == edge_x
                    or new_y == edge_y
                ):
                    # here the boundary is laid by cells that are larger than its neighbours,
                    # all cells in the first row and the first column will go into pacific
                    # all cells in the last row and the last column will go into pacific
                    dfs(new_x, new_y, ocean)

    rows = len(matrix)
    if rows > 0:
        cols = len(matrix[0])
        if cols > 0:
            pacific = []
            atlantic = []
            visited = set()
            # start pacific search from top left corner
            dfs(0, 0, "P")
            # clear visited for atlantic since it might overlap with pacific
            visited = set()
            # start pacific search from bottom right corner
            dfs(rows - 1, cols - 1, "A")

            return set(pacific).intersection(set(atlantic))


test = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(pacificAtlantic(test))
