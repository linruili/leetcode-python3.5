def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    def unique(L):
        s = set()
        for x in L:
            if '1'<=x<='9' and x in s:
                return False
            else:
                s.add(x)
        return True

    for i in range(9):
        if unique(board[i])==False:
            return False
        L = []
        for j in range(9):
            L.append(board[j][i])
        if unique(L)==False:
            return False
    for i in range(3):
        for j in range(3):
            L = []
            for k in range(3):
                for w in range(3):
                    L.append(board[i*3+k][j*3+w])
            if unique(L)==False:
                return False
    return True

print(isValidSudoku(["......5..",".........",".........","93..2.4..","..7...3..",".........","...34....",".....3...",".....52.."]))