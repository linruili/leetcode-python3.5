def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    i0 , i1 ,i2 = 0, 0 , len(nums)-1
    while i0<=i2:
        if nums[i0]==1:
            i0 += 1
        elif nums[i0]==0:
            nums[i0] , nums[i1] = nums[i1] , nums[i0]
            i0 += 1
            i1 += 1
        else:
            nums[i0] , nums[i2] = nums[i2] , nums[i0]
            i2 -= 1
