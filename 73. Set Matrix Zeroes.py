def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                for k in range(len(matrix[i])):
                    matrix[i][k] = float(matrix[i][k])
                for k in range(len(matrix)):
                    matrix[k][j] = float(matrix[k][j])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if isinstance(matrix[i][j] , float):
                matrix[i][j] = 0

L = [[0]]
setZeroes(L)
print(L)

