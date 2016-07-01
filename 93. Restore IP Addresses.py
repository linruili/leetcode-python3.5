def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def recursion(k ,totalLen):
        if totalLen>len(s) or (k==5 and totalLen!=len(s)):
            return
        if k==5 and totalLen==len(s):
            ss = sublen[0]
            for i in range(1,4):
                ss += '.'+sublen[i]
            ans.append(ss)
            return
        for i in range(1,4):
            if totalLen+i<=len(s):
                subs = s[totalLen:totalLen+i]
                if 0<=int(subs)<=255:
                    sublen.append(subs)
                    recursion(k+1 , totalLen+i )
                    sublen.pop()
                    if int(subs)==0:
                        break
    sublen , ans = [] , []
    recursion(1 , 0)
    return ans


print(restoreIpAddresses("010010"))