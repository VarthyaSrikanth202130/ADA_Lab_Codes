"""Q. Program to implement n queens algorithm using Backtracking"""

from __future__ import annotations
solution = []
def is_safe(board: list[list[int]], row: int, column: int) -> bool:
    #returns a boolean value True if it is safe to place a queen
    for i in range(len(board)):
        if board[row][i] == 1:
            return False
    for i in range(len(board)):
        if board[i][column] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve(board: list[list[int]], row: int) -> bool:
    if row >= len(board):
        solution.append(board)
        printboard(board)
        print()
        return True
    for i in range(len(board)):  #iterates through each column
        if is_safe(board, row, i):
            board[row][i] = 1
            solve(board, row + 1)
            board[row][i] = 0
    return False

def printboard(board: list[list[int]]) -> None:
    #Prints the boards that have a successful combination
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

n=int(input("The no. of queens: "))
board = [[0 for i in range(n)] for j in range(n)]
solve(board, 0)
print("The total no. of solutions are :", len(solution))