def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    for i in range(len(nums)):
        while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1]!=nums[i]:
            nums[nums[i]-1] , nums[i] = nums[i] , nums[nums[i]-1]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1

print(firstMissingPositive([1,2]))