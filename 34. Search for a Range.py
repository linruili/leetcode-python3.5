def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    i , j = 0 , len(nums)-1
    while i<=j:
        mid = (i+j)//2
        if nums[mid]>target:
            j = mid-1
        elif nums[mid]<target:
            i = mid+1
        else:
            i1 , j1 = i , mid
            i2 , j2 = mid , j
            while i1<=j1:
                mid = (i1+j1)//2
                if nums[mid]<target:
                    i1 = mid+1
                elif mid==0 or nums[mid-1]!=target:
                    i1 = mid
                    break
                else:
                    j1 = mid-1
            while i2<=j2:
                mid = (i2+j2)//2
                if nums[mid]>target:
                    j2 = mid-1
                elif mid==len(nums)-1 or nums[mid+1]!=target:
                    j2 = mid
                    break
                else:
                    i2 = mid+1
            return [i1 , j2]
    return [-1,-1]

print(searchRange([5, 7, 7, 8, 8, 10],8))
