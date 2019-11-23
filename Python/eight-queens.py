#The eight queens problem is the problem of placing eight queens on an 8×8 chessboard such that none of them attack one another (no two are in the same row, column, or diagonal).

#https://www.geeksforgeeks.org/python-program-for-n-queen-problem-backtracking-3/

board = list();

for i in range (0,8):
    new = []
    for j in range (0,8):
        new.append(0)
    board.append(new)

print(board[0][0])

