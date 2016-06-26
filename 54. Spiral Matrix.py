def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    sm , sn = 0 , 0
    L = []
    if not matrix:
        return L
    m , n = len(matrix) , len(matrix[0])
    while True:
        for i in range(sn , n):
            L.append(matrix[sm][i])
        sm += 1
        if sm > m-1:
            break
        for i in  range(sm , m):
            L.append(matrix[i][n-1])
        n -= 1
        if sn > n-1:
            break
        for i in range(n-1 , sn-1 , -1):
            L.append(matrix[m-1][i])
        m -= 1
        if sm > m-1:
            break
        for i in range(m-1 , sm-1 , -1):
            L.append(matrix[i][sn])
        sn += 1
        if sn > n-1:
            break
    return L

m = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(spiralOrder(m))