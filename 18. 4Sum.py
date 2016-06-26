def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    if len(nums)<4:
        return []
    nums.sort()
    res = []
    w = 3
    while w < len(nums):
        k = 2
        while k < w:
            i , j = 0 , k-1
            while i<j:
                n = nums[i] + nums[j] + nums[k] + nums[w]
                if n > target:
                    j -= 1
                elif n < target:
                    i += 1
                else:
                    if [nums[i] , nums[j] ,nums[k] , nums[w]] not in res:
                        res.append([nums[i] , nums[j] ,nums[k] , nums[w]] )
                    i , j = i+1 ,j-1
            k += 1
        w += 1
    return res

print(fourSum([1, 0, -1, 0, -2, 2] , 0))
