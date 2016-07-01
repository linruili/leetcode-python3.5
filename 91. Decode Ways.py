def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    def could2 (i,j):
        if int(s[i])==1 or ( int(s[i])==2 and 0<=int(s[j])<=6 ):
            if int(s[j])==0:
                return 2
            else:
                return 1
        elif int(s[j])==0:
            return -1
        return 0
    ans = []
    if not s or s[0]=='0':
        return 0
    ans.append(1)
    if len(s)>=2:
        if could2(0,1)==1:
            ans.append(2)
        elif could2(0,1)==2:
            ans.append(1)
        elif could2(0,1)==-1:
            return 0
        else:
            ans.append(1)
    for i in range(2,len(s)):
        if could2(i-1,i)==1:
            ans.append(ans[i-2]+ans[i-1])
        elif could2(i-1,i)==-1:
            return 0
        elif could2(i-1,i)==2:
            ans.append(ans[i-2])
        else:
            ans.append(ans[i-1])
    return ans[-1]

print(numDecodings("20"))

