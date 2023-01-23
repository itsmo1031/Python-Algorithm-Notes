example = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

'''Flip a matrix'''


def flip_a_matrix(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][r] = matrix[r][c]

    return res


print(flip_a_matrix(example))
''' example result
[
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]
'''
