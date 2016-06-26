def generate( numRows):
    L = []
    if numRows ==0:
        return L
    a = [1]
    L.append(a)
    for i in range(2,numRows+1):
        b = a[:]
        b.append(0)
        a = [b[j-1] + b[j] for j in range(len(b))]
        L.append(a)
    return L

print(generate(5))


