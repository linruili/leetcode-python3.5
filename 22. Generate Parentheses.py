def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    def recursion(l,r,L,ans):
        if l==0 and r==0:
            ans.append("".join(L))
            return
        if l>0:
            L.append("(")
            recursion(l-1, r+1, L,ans)
            L.pop()
        if r>0:
            L.append(")")
            recursion(l, r-1, L, ans)
            L.pop()
    ans = []
    recursion(n, 0, [], ans)
    return ans
