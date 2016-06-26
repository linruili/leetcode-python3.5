def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    for i in range(len(nums) - 1 , 0 ,-1):
        if nums[i]>nums[i-1]:
            for j in range(len(nums)-1 , i-1 , -1):
                if nums[j]>nums[i-1]:
                    nums[i-1] ,nums[j] = nums[j] , nums[i-1]
                    break
            j = len(nums) - 1
            while i<j:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
            return
    i = 0
    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

L = [1,3,2]
nextPermutation(L)
print(L)

