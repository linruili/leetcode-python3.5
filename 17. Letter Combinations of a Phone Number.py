def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    def recursion(k):
        if k==len(digits):
            ans.append("".join(L))
            return
        letters = letterList[int(digits[k])]
        for c in letters:
            L.append(c)
            recursion(k+1)
            L.pop()
    ans , L = [] , []
    letterList = [' ','*',"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    if digits=="":
        return []
    recursion(0)
    return ans

print(letterCombinations(""))
