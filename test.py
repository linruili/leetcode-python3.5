s = [1,3,1,2]
# for i in range(len(s)):
i = 0
while i<len(s):
    if i==1 :
        s.pop(i)
    if i==3:
        print(s[i])
    i += 1
print(s)