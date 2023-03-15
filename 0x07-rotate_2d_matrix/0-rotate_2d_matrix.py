#!/usr/bin/python3
"""
rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it 90 degrees clockwise
    """
    N = len(matrix)

    for x in range(N):
        for ran in range(x, N):
            rot = matrix[x][ran]
            matrix[x][ran] = matrix[ran][x]
            matrix[ran][x] = rot

    for x in range(N):
        for ran in range(N // 2):
            rot = matrix[x][ran]
            matrix[x][ran] = matrix[x][N - 1 - ran]
            matrix[x][N - 1 - ran] = rot
