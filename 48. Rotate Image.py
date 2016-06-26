def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    d = 0
    n = len(matrix)
    while d<n//2:
        for i in range(n-2*d-1):
            matrix[d][d+i] , matrix[d+i][n-1-d] , matrix[n-1-d][n-1-d-i] , matrix[n-1-d-i][d] = \
                matrix[n-1-d-i][d] , matrix[d][d+i] , matrix[d+i][n-1-d] , matrix[n-1-d][n-1-d-i]
        d += 1

L =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(L)
print(L)

