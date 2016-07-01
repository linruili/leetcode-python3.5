def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    bitnum = [0]*32
    ans ,count = 0 , 0

    for i in range(32):
        for x in nums:
            if x<0:
                x = -x
                count += 1
            bitnum[i] += (x>>i)&1
        ans |= (bitnum[i]%3)<<i
    if count%3 != 0:
        ans = -ans
    return ans


print(singleNumber([-4]))