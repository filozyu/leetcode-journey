# Recursion
def spiralOrder(matrix):
    """
    Recursion on layers
    Time: O(N); N the number of elements in matrix
    Space: O( ceil( min (m , n) / 2) ); m, n = #rows, #columns in matrix (recursion stack)
    """
    result = []
    if not matrix or not matrix[0]:
        return result
    m = len(matrix)
    n = len(matrix[0])
    spiral_one_round(matrix, 0, m, n, result)
    return result


def spiral_one_round(matrix, start, m, n, result):
    for i in range(start, n):
        result.append(matrix[start][i])
    for j in range(start + 1, m):
        result.append(matrix[j][n - 1])
    # if the inner matrix in this iteration has more than two rows
    if m - start > 1:
        for k in range(n - 2, start - 1, -1):
            result.append(matrix[m - 1][k])
        # if the inner matrix in this iteration has more than two columns
        if n - start > 1:
            for l in range(m - 2, start, -1):
                result.append(matrix[l][start])
    start += 1
    m -= 1
    n -= 1
    # if the next inner matrix is not empty, carry on with the next layer
    if start < min(m, n):
        spiral_one_round(matrix, start, m, n, result)


test_1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
test_2 = [[4]]
test_3 = [[4, 5, 6]]
test_4 = [[4], [5], [6]]
print(spiralOrder(test_4))
