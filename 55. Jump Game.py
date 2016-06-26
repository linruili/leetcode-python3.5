def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True
    for i in range(len(nums)-2):
        if nums[i] == 0:
            return False
        nums[i+1] = max(nums[i]-1 , nums[i+1])
    if nums[-2] > 0:
        return True
    else:
        return False

print(canJump([3,2,1,0,4]))


