example = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

'''Rotate a maxtrix by -90 degree using zip'''


def rotate_a_matrix_by_minus_90_degree_using_zip(matrix):
    res = [*map(list, zip(*matrix))][::-1]
    return res


print(rotate_a_matrix_by_minus_90_degree_using_zip(example))
''' example result
[
    [4, 8, 12],
    [3, 7, 11],
    [2, 6, 10],
    [1, 5, 9]
]
'''
