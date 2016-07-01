def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    citations.sort(reverse=True)
    for i in range(len(citations)-1 , -1 ,-1):
        if i+1<=citations[i]:
            return i+1
    return 0



