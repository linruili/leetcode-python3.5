class Solution(object):
    def status(self, x, y, board):  # self
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]):
            return 0
        return board[x][y] & 1

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        for x in range(len(board)):
            for y in range(len(board[x])):
                life = 0
                for z in range(8):
                    life += self.status(x + dx[z], y + dy[z], board)
                if board[x][y] + life == 3 or life == 3:
                    board[x][y] |= 2
        for x in range(len(board)):
            for y in range(len(board[x])):
                board[x][y] >>= 1

c = Solution()
L = [[1,0],[0,1],[1,1]]
c.gameOfLife(L)
print(L)