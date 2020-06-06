# searching, binary search, divide and conquer


def searchMatrix(matrix, target):
    """
    Brute force
    Time: O(mn) m - number of rows; n - number of columns
    Space: O(1)
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if target == matrix[i][j]:
                return True
    return False


def searchMatrix_binary(matrix, target):
    """
    Loop through the diagonal, and for each element, conduct a binary search on the row and one on the column
    Time: O(nlogn + mlogm) see below for analysis
    Space: O(1)
    """
    if not matrix:
        return False
    num_row = len(matrix)
    num_col = len(matrix[0])
    # loop through the diagonal
    # Time: O(log(m!) + log(n!)) = O(mlogm + nlogn)
    for diag in range(min(num_row, num_col)):
        # initialise the binary search
        # Note a row has length num_col and a column has length num_row
        # both row and column searches will start from diag, since the previous elements have already been checked
        row_lo, row_hi = diag, num_col - 1
        col_lo, col_hi = diag, num_row - 1

        # binary search on the current row
        # Time: O(log(n-diag))
        while row_lo <= row_hi:
            row_mid = (row_lo + row_hi) // 2
            if matrix[diag][row_mid] == target:
                return True
            elif matrix[diag][row_mid] < target:
                row_lo = row_mid + 1
            else:
                row_hi = row_mid - 1

        # binary search on the current column
        # Time: O(log(m-diag))
        while col_lo <= col_hi:
            col_mid = (col_lo + col_hi) // 2
            if matrix[col_mid][diag] == target:
                return True
            elif matrix[col_mid][diag] < target:
                col_lo = col_mid + 1
            else:
                col_hi = col_mid - 1

    return False


def searchMatrix_increment(matrix, target):
    """
    Search from top right corner (or we can search from the bottom left corner)
    When comparing the target with the current element, one has to ensure there is only one option in each of the
    possible cases (equal, greater, less); therefore we cannot start from the top left or the bottom right corners
    Time: O(m+n)
    Space: O(1)
    """
    if not matrix:
        return False
    num_row = len(matrix)
    num_col = len(matrix[0])
    # initialise the search position to be the top right corner
    curr_row, curr_col = 0, num_col - 1
    while curr_row < num_row and curr_col > -1:
        # found the target, return
        if matrix[curr_row][curr_col] == target:
            return True
        # current number larger than target, move left
        elif matrix[curr_row][curr_col] > target:
            curr_col -= 1
        # current number smaller than target, move right
        else:
            curr_row += 1
    # if we reach here it means the target is not found in the matrix
    return False
