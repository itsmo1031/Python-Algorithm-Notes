example = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

'''Flip a matrix using zip'''


def flip_a_matrix_using_zip(matrix):
    res = [*map(list, zip(*matrix))]
    return res


print(flip_a_matrix_using_zip(example))
''' example result
[
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]
'''
