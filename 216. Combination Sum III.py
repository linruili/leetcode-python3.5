def combinationSum3( k, n):
    """
    :type k: int
    :type n: int
    :rtype: List[List[int]]
    """
    L = []
    a = []

    def sum3(begin , k , n):
        if 9-begin+1<k :
            return

        if k ==0:
            sum = 0
            for num in a:
                sum +=  num
            if sum == n:
                L.append(a[:])
            return

        for i in range(begin , 9-k+2 ):
            a.append(i)
            sum3(i+1 , k-1 , n)
            a.pop()

    sum3(1, k, n)
    return L

print(combinationSum3(3,9))
