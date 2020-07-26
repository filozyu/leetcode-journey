def solve(board):
    """
    DFS with marker to checker if an island touches the edge
    Time: O(n) loop through the board, n: number of letters in the board
    Space: O(n) visited, recursion stack and process_list
    """

    def dfs(pos_x, pos_y):

        # touch_edge is from outer scope (function solve) to indicate
        # whether the current block of "O"s touches the boundary of the board
        # if touch_edge is set to True, the whole block will be left unchanged (process_list will be emptied after dfs)
        nonlocal touch_edge

        visited[pos_x][pos_y] = 1
        process_list.append((pos_x, pos_y))

        if not (0 < pos_x < rows - 1 and 0 < pos_y < cols - 1):
            # touches the boundary
            touch_edge = True

        # up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for d in directions:
            temp_x = pos_x + d[0]
            temp_y = pos_y + d[1]
            # check if coordinates legal and if there is any connected "O"
            if (
                0 <= temp_x < rows
                and 0 <= temp_y < cols
                and board[temp_x][temp_y] == "O"
            ):
                if visited[temp_x][temp_y] == 1:
                    # if already seen, skip
                    continue
                dfs(temp_x, temp_y)

    def reverse(pos):
        for p in pos:
            board[p[0]][p[1]] = "X"

    rows = len(board)
    if rows > 0:
        cols = len(board[0])
        if cols > 0:
            # initialise visited
            visited = [[0] * cols for _ in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    if not visited[i][j] and board[i][j] == "O":
                        touch_edge = False
                        process_list = []
                        dfs(i, j)
                        # only empty process_list if the block has touched edge at some point
                        if touch_edge:
                            process_list = []
                        else:
                            reverse(process_list)


def solve_fast(board):
    """
    DFS from the boundaries
    Time: O(n)
    Space: O(n) in the worst case recursion stack could be O(n)
    """

    def dfs(pos_x, pos_y):
        # only do dfs starting from the letters on the four edges
        # assign "E" to indicate edge
        board[pos_x][pos_y] = "E"
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            temp_x = pos_x + d[0]
            temp_y = pos_y + d[1]
            # check if coordinates legal and if there is any connected "O"
            if (
                0 <= temp_x < rows
                and 0 <= temp_y < cols
                and board[temp_x][temp_y] == "O"
            ):
                dfs(temp_x, temp_y)

    edges = []
    rows = len(board)
    if rows > 0:
        cols = len(board[0])
        if cols > 0:
            # get edges
            edges += [[0, c] for c in range(cols)]
            edges += [[rows - 1, c] for c in range(cols)]
            edges += [[r, 0] for r in range(rows)]
            edges += [[r, cols - 1] for r in range(rows)]

        for pos_x, pos_y in edges:
            # dfs from edges
            if board[pos_x][pos_y] == "O":
                dfs(pos_x, pos_y)

        for i in range(rows):
            for j in range(cols):
                # for all letters "E", they are the blocks connected to the boundaries
                if board[i][j] == "E":
                    board[i][j] = "O"
                # flip the blocks not connected to the boundaries
                elif board[i][j] == "O":
                    board[i][j] = "X"


test_1 = [
    ["O", "X", "O", "O", "O", "X"],
    ["O", "O", "X", "X", "X", "O"],
    ["X", "X", "X", "X", "X", "O"],
    ["O", "O", "O", "O", "X", "X"],
    ["X", "X", "O", "O", "X", "O"],
    ["O", "O", "X", "X", "X", "X"],
]

solve_fast(test_1)
for row in test_1:
    print(row)
