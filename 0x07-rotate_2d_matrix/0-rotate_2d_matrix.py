#!/usr/bin/python3
'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''Given an n x n 2D matrix, rotate it 90 degrees clockwise'''

    n = len(matrix)
    # firstly transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # secondly reverse the rows
    for row in matrix:
        row.reverse()
