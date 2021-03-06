def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """
    q = [1]
    i2, i3, i5 = 0, 0, 0
    while n>len(q):
        m2 , m3 , m5 = q[i2]*2 , q[i3]*3 , q[i5]*5
        m = min(m2,m3,m5)
        q += m,
        if m==m2:
            i2 += 1
        if m==m3:
            i3 += 1
        if m==m5:
            i5 += 1
    return q[-1]

print(nthUglyNumber(11))
