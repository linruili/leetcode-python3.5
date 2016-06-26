def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def combinationSum_recur(begin , sum):
        if sum<0 :
            return
        if sum ==0:
            result.append(L[:])
        for i in range(begin , len(candidates)):
            L.append(candidates[i])
            combinationSum_recur(i , sum-candidates[i])
            L.pop()

    candidates.sort()
    result = []
    L = []
    combinationSum_recur(0,target)
    return result

print(combinationSum([2,3,6,7] , 7))