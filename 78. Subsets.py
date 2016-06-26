def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def subsets_rec(begin):
        result.append(L[:])
        for i in range(begin, len(nums)):
            L.append(nums[i])
            subsets_rec(i + 1)
            L.pop()

    nums.sort()
    result = []
    L = []
    subsets_rec(0)
    return result

print(subsets([1,2,3]))
