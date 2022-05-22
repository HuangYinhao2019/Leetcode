def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    d = [[] for _ in range(10)]
    for i in range(9):
        for j in range(9):
            if board[i][j] != ".":
                n = int(board[i][j])
                t = (i, j, (i / 3) * 10 + (j / 3))
                for k in range(len(d[n])):
                    if d[n][k][0] == t[0] or d[n][k][1] == t[1] or d[n][k][2] == t[2]:
                        return False
                d[n].append(t)
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]
))