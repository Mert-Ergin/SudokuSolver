import numpy as np

board = [\
[0, 4, 0, 0, 0, 0, 1, 7, 9], 
[0, 0, 2, 0, 0, 8, 0, 5, 4], 
[0, 0, 6, 0, 0, 5, 0, 0, 8], 
[0, 8, 0, 0, 7, 0, 9, 1, 0], 
[0, 5, 0, 0, 9, 0, 0, 3, 0], 
[0, 1, 9, 0, 6, 0, 0, 4, 0], 
[3, 0, 0, 4, 0, 0, 7, 0, 0], 
[5, 7, 0, 1, 0, 0, 2, 0, 0], 
[9, 2, 8, 0, 0, 0, 0, 6, 0]]


def valid(board, num, row, col):
    for n in range(9):
        # scan through the row
        if board[row][n] == num and n != col:
            return False
        # scan through the column
        if board[n][col] == num and n != row:
            return False
    # Check boxes
    sr = (row//3) * 3
    sc = (col//3) * 3
    for i in range(sr, sr+3):
        for j in range(sc, sc+3):
            if (board[i][j] == num) and (i != row or j != col):
                return False
    return True


def solve():
    global board
    for c in range(9):
        for r in range(9):
            if board[r][c] == 0:
                for i in range(1, 10):
                    if valid(board, i, r, c):
                          board[r][c] = i
                          solve()
                        # 
                          board[r][c] = 0

                return       
    print(np.matrix(board))

if __name__ == "__main__":
    print(np.matrix(board))
    solve()

    pass
