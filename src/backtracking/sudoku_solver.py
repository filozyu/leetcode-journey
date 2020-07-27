from collections import defaultdict


def board_to_coordinates(board):
    # return the coordinates to fill
    assert len(board) == 9

    coordinates = []

    for i in range(9):
        assert len(board[i]) == 9
        for j in range(9):
            if board[i][j] == ".":
                coordinates.append((i, j))

    return coordinates


def initialise_block_dict(board):
    # initialise the dicts to hold filled values
    row_dict = defaultdict(set)
    col_dict = defaultdict(set)
    block_dict = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                row_dict[i].add(board[i][j])
                col_dict[j].add(board[i][j])
                block_dict[(i // 3, j // 3)].add(board[i][j])

    return row_dict, col_dict, block_dict


def solveSudoku(board):
    """
    Backtracking
    Time: O(1) since the board size is fixed, but the upper bound is (9!)^9, suppose there are 81 positions to fill
    Space: O(1) again since the board size is fixed, the extra space we used are recursion stack and three dicts
    """

    def backtrack(pos):

        nonlocal find_sol

        if pos == len(coord):
            # if find_sol is True, stop backtracking and exit the recursion
            find_sol = True
            return

        # the current coordinate on board to fill
        fill_x, fill_y = coord[pos][0], coord[pos][1]

        for num in range(1, 10):

            # the candidate used to fill the current space
            candidate = str(num)

            if (
                candidate not in row_dict[fill_x]
                and candidate not in col_dict[fill_y]
                and candidate not in block_dict[(fill_x // 3, fill_y // 3)]
            ):
                # candidate is legal if it meets the rules
                row_dict[fill_x].add(candidate)
                col_dict[fill_y].add(candidate)
                block_dict[(fill_x // 3, fill_y // 3)].add(candidate)

                # fill candidate on the board
                board[coord[pos][0]][coord[pos][1]] = candidate

                # look at the next empty space
                backtrack(pos + 1)

                # only undo the selection if it does not lead to a valid solution
                # since we need to change board in place, so we don't need to set back if the solution is correct
                if not find_sol:
                    board[coord[pos][0]][coord[pos][1]] = "."
                    row_dict[fill_x].remove(candidate)
                    col_dict[fill_y].remove(candidate)
                    block_dict[(fill_x // 3, fill_y // 3)].remove(candidate)

    coord = board_to_coordinates(board)

    row_dict, col_dict, block_dict = initialise_block_dict(board)

    find_sol = False

    backtrack(0)


test = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
solveSudoku(test)
for r in test:
    print(r)
