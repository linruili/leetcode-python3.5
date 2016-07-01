import collections
def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    if strs[0] == "":
        return [[""]]
    L = []
    d = collections.defaultdict(list)
    for x in strs:
        d["".join(sorted(x))].append(x)
    for x in d.values():
        x.sort()
        L.append(x)
    return L

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
