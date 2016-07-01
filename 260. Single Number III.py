def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    xor = 0
    for x in nums:
        xor ^= x
    lowbit = xor& (-xor)  # 从低位向高位，第一个非0位所对应的数字
    a , b = 0, 0
    for x in nums:
        if x&lowbit:
            a ^= x
        else:
            b ^= x
    return [a,b]
