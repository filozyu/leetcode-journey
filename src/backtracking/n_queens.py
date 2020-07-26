def coord_to_board(coordinates, n):
    # helper function to convert coordinates to board, queens are represented by "Q"s
    board = []
    coordinates.sort(key=lambda x: x[1])
    for c in coordinates:
        c_x = c[0]
        left = "." * c_x
        right = "." * (n - c_x - 1)
        curr_row = left + "Q" + right
        board.append(curr_row)

    return board


def solveNQueens(n):
    """
    Backtracking, add queens row by row, search for columns in each row
    Time: O(n!) for every row we went down, the choice of columns reduces by one
    Space: O(n) for the occupied columns, two diagonals, curr_res and recursion stack
    """

    def backtrack(curr_res, search_row):
        # exit recursion if we have gathered n coordinates
        if len(curr_res) == n:
            res.append(curr_res[:])

        # search for the potential row in the current row (search_row)
        for j in range(n):
            # check for valid columns
            if (
                j not in occupied_cols
                and search_row + j not in occupied_off_diag
                and search_row - j not in occupied_diag
            ):

                # append valid queen position to curr_res
                curr_res.append((search_row, j))

                # update occupied info
                occupied_cols.add(j)
                occupied_diag.add(search_row - j)
                occupied_off_diag.add(search_row + j)

                # search for the next queen (in the next row: search_row + 1)
                backtrack(curr_res, search_row + 1)

                # undo selection, try other columns in search_row
                curr_res.pop()

                # remove the occupied info
                # time of removing from a set is O(1) on average
                occupied_cols.remove(j)
                occupied_diag.remove(search_row - j)
                occupied_off_diag.remove(search_row + j)

    # since we are placing queens row by row,
    # we need to check
    # 1. the columns they occupy
    # 2. the (main) diagonal they occupy
    # 3. the off diagonal they occupy
    occupied_cols = set()
    occupied_diag = set()
    occupied_off_diag = set()

    # the solutions (coordinates of the queens) are stored in res
    res = []

    backtrack([], 0)

    # convert res to board
    all_boards = []
    for r in res:
        board = coord_to_board(r, n)
        all_boards.append(board)

    return all_boards


test_n = 4
print(solveNQueens(test_n))
