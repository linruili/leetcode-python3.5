def nthSuperUglyNumber(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    ans = [1]
    index = []
    for i in range(len(primes)):
        index.append(0)
    while n>len(ans):
        min = primes[0]*ans[index[0]]
        for i in range(len(primes)):
            if primes[i]*ans[index[i]] < min:
                min = primes[i]*ans[index[i]]
        for i in range(len(primes)):
            if primes[i]*ans[index[i]] == min:
                index[i] += 1
        ans += min,
    return ans[-1]

print(nthSuperUglyNumber(10,[3,5,7,13,17,19,29,31,37,41,47,59,71,73,79,83,97,127,131,137]))
