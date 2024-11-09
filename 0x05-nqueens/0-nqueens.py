#!/usr/bin/python3
'''N queens puzzle'''
import sys


class NQueens:
    '''Class for solving N queens puzzle'''

    def __init__(self, N):
        '''Init method'''
        self.N = N
        self.col = set()
        self.posDiag = set()  # (row + col)
        self.negDiag = set()  # (row - col)
        self.solutions = []
        self.current_solution = []

    def backtrack(self, row):
        '''Backtrack method to find all solutions'''
        if row == self.N:
            # When we reach N rows, we've found a valid solution
            self.solutions.append(self.current_solution[:])
            return

        for col in range(self.N):
            if (col in self.col or (row + col) in self.posDiag or (row - col) in self.negDiag):
                continue

            # Add queen position
            self.col.add(col)
            self.posDiag.add(row + col)
            self.negDiag.add(row - col)
            self.current_solution.append([row, col])

            # Move to next row
            self.backtrack(row + 1)

            # Remove queen position (backtrack)
            self.col.remove(col)
            self.posDiag.remove(row + col)
            self.negDiag.remove(row - col)
            self.current_solution.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    nq = NQueens(N)
    nq.backtrack(0)
    for solution in nq.solutions:
        print(solution)
