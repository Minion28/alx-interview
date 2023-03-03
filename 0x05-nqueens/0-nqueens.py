#!/usr/bin/python3
"""
A program that solves the N queens problem
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (num >= 4):
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """Solution for n queens"""
    column = set()
    position = set()
    non = set()

    output = []
    board = [[] for n in range(n)]

    def backtrack(row):
        """function for recursion"""
        if row == n:
            copy = board.copy()
            output.append(copy)
            return


        for c in range(n):

            if c in column or (row + c) in position or (row - c) in non:
                continue

            column.add(c)
            position.add(row + c)
            non.add(row - c)

            board[row] = [row, c]


            backtrack(row + 1)

            column.remove(c)
            position.remove(row + c)
            non.remove(row - c)
            board[row] = []

    backtrack(0)

    return output


if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)
