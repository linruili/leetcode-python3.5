def uniquePathsWithObstacles( obstacleGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    result = [([1] * n) for i in range(m)]
    result[0][0] = 1 - obstacleGrid[0][0]
    for i in range(1, m):
        if obstacleGrid[i][0]==0 and result[i-1][0]==1:
            result[i][0] = 1
        else:
            result[i][0] = 0
    for i in range(1,n):
        if obstacleGrid[0][i]==0 and result[0][i-1]==1:
            result[0][i] = 1
        else:
            result[0][i] = 0
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                result[i][j] = 0
            else:
                result[i][j] = result[i - 1][j] + result[i][j - 1]
    return result[m - 1][n - 1]

L = [
  [0,0],
  [1,0],
]
print(uniquePathsWithObstacles(L))