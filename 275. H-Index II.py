def hIndex(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    i , j = 0 , len(citations)-1
    while i<=j:
        mid = (i+j)//2
        if mid+1<=citations[len(citations)-1-mid]:
            i = mid+1
        else:
            j = mid-1
    return i

