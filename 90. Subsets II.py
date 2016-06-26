def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def subsets_rec(begin):
        result.append(L[:])
        i = begin
        while i<len(nums):
            L.append(nums[i])
            subsets_rec(i + 1)
            L.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i += 1
            i += 1


    nums.sort()
    result = []
    L = []
    subsets_rec(0)
    return result

print(subsetsWithDup([1,2,2,1]))