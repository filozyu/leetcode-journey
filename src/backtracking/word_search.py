# Backtracking
def exist(board, word):
    """
    Backtracking
    Time: O(n*4^w) n - number of cells on the board, w - length of word
    Space: O(w) depth of the recursion stack (backtracking will be called at most w times)
    """
    height = len(board)
    width = len(board[0])
    # the following two loops: O(n)
    for h in range(height):
        for w in range(width):
            # backtracking at each cell will at worst run: O(4^w)
            res = backtrack(board, word, [h, w])
            if res:
                return True
    return False


def backtrack(board, word, index):
    # every time check one letter in the word, then for the rest of the word, use recursion
    height = len(board)
    width = len(board[0])
    # the word has been found if the following condition is true, terminate the algorithm
    if len(word) == 0:
        return True
    # the boundary checks should be done within the recursion
    if (
        index[0] < 0
        or index[0] >= height
        or index[1] < 0
        or index[1] >= width
        or board[index[0]][index[1]] != word[0]
    ):
        return False
    # if we are here, it means that board[index[0]][index[1]] is word[0]
    # since we cannot use any word twice, we mark the visited cell
    board[index[0]][index[1]] = "visited"
    # for all four directions
    # think of this as growing a tree with w layers (w the length of the word),
    # where each node has four neighbours, if the tree is fully grown,
    # there are in total 4^w different leaf nodes and therefore 4^w different paths
    for row_next, col_next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        res = backtrack(board, word[1:], [index[0] + row_next, index[1] + col_next])
        # if res is true, we have found the word in question, terminate the algorithm
        if res:
            break
    # recover the marked visited cell
    board[index[0]][index[1]] = word[0]
    return res


test_b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_w = "ABCCED"
print(exist(test_b, test_w))
