example = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

'''Rotate a matrix by 90 degree'''


def rotate_a_matrix_by_90_degree(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = matrix[r][c]

    return res


print(rotate_a_matrix_by_90_degree(example))
''' example result
[
    [9, 5, 1],
    [10, 6, 2],
    [11, 7, 3],
    [12, 8, 4]
]
'''
