def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    def toLower(s):
        if 'a'<=s<='z' or 'A'<=s<='Z' or '0'<=s<='9':
            return s.lower()
        else:
            return None

    if not s:
        return True
    i , j = 0 , len(s)-1
    while i<=j:
        while i <= j and not toLower(s[i]):
            i += 1
        while i <= j and not toLower(s[j]):
            j -= 1
        if i<=j and toLower(s[i]) != toLower(s[j]):
            return False
        i , j = i+1 , j-1
    return True
