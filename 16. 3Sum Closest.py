def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    k = 2
    c = nums[0] + nums[1] + nums[2]
    while k<len(nums):
        i ,j = 0 , k-1
        while i<j:
            n = nums[i] + nums[j] + nums[k]
            if abs(n - target) < abs(c - target):
                c = n
            if n==target:
                return n
            elif n>target:
                j -= 1
            else:
                i += 1
        k += 1
    return c

print(threeSumClosest([0,0,0] , 1))

