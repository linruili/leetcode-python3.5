def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    d1 , d2 = {} ,{}
    if len(s)!=len(t) :
        return False
    for i in range(len(s)):
        if s[i] in d1 and d1[s[i]] != t[i]:
             return False
        elif t[i] in d2 and d2[t[i]] != s[i]:
            return False
        else:
            d1[s[i]] = t[i]
            d2[t[i]] = s[i]
    return True

