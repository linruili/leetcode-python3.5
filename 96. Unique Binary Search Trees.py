def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    ans = 1
    for i in range(n+1 , 2*n+1):
        ans *= i
    for i in range(1,n+1):
        ans //= i
    ans //= n+1
    return ans

        