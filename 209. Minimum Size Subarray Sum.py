def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    MAXLEN = 99999999
    begin , end , sum ,min = 0, 0, 0 ,MAXLEN
    while end<=len(nums)-1:
        while sum < s and end<len(nums):
            sum += nums[end]
            end += 1
        if sum>=s and min > end-begin :
            min = end - begin
        while sum >= s :
            sum -= nums[begin]
            begin += 1
            if sum >= s and min > end-begin:
                min = end - begin
    if min == MAXLEN:
        min = 0
    return min

print(minSubArrayLen(7 ,[2,3,1,2,4,3]))

