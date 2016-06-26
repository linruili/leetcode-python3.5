def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    result = [[1]*n]*m
    for i in range(1 , m):
        for j in range(1 , n):
            result[i][j] = result[i-1][j] + result[i][j-1]
    return result[m-1][n-1]

print(uniquePaths(2,4))

