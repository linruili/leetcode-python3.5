def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #note:you can assuem that you can alaways reach the last index
    maxn ,maxj ,ans = 0 ,0 ,0
    for i in range(len(nums)-1):
        maxn = max(nums[i]+i , maxn)
        if i==maxj:
            maxj , ans = maxn , ans+1
    return ans

