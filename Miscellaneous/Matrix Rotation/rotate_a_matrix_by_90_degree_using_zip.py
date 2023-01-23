example = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

'''Rotate a matrix by 90 degree using zip'''


def rotate_a_matrix_by_90_degree_using_zip(matrix):
    res = [*map(list, zip(*matrix[::-1]))]
    return res


print(rotate_a_matrix_by_90_degree_using_zip(example))
''' example result
[
    [9, 5, 1],
    [10, 6, 2],
    [11, 7, 3],
    [12, 8, 4]
]
'''
