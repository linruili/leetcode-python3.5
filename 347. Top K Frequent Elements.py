import collections
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = collections.defaultdict(int)
    for x in nums:
        d[x] += 1
    freList = [[] for i in range(len(nums)+1)]
    for x in d:
        freList[d[x]].append(x)
    ans = []
    for i in range(len(freList)-1 , -1 ,-1):
        ans += freList[i]
    return ans[:k]

