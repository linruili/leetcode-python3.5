def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    def combinationSum_recur(begin, sum):
        if sum < 0:
            return
        if sum == 0:
            result.append(L[:])
        i = begin
        while i<len(candidates):
            L.append(candidates[i])
            combinationSum_recur(i+1, sum - candidates[i])
            L.pop()
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            i += 1


    candidates.sort()
    result = []
    L = []
    combinationSum_recur(0, target)
    return result
