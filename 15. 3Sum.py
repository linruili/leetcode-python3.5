def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res = []
    k = 2
    while k<len(nums):
        i , j = 0 , k-1
        while i<j :
            if nums[i]+nums[j]+nums[k] == 0:
                if [nums[i] , nums[j] , nums[k]] not in res:
                    res.append([nums[i] , nums[j] , nums[k]])
                while i<j and (nums[i]==nums[i+1] and nums[j]==nums[j-1]):
                    i += 1
                    j -= 1
                i += 1
                j -= 1
            elif nums[i]+nums[j]+nums[k] > 0:
                j -= 1
            else:
                i += 1
        k += 1
    return res

s = [-2, 0, 0 ,0,0,0 ,0, 0, 1,1,1,1, 2]
print(threeSum(s))