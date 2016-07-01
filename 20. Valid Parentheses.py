def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for i in range(len(s)):
        if s[i]=='(' or s[i]=='[' or s[i]=='{':
            stack.append(s[i])
        if s[i]==')' or s[i]=='}' or s[i]==']':
            if not stack:
                return False
            if s[i]==')' and stack[-1]=='(':
                stack.pop()
            elif s[i]==']' and stack[-1]=='[':
                stack.pop()
            elif s[i]=='}' and stack[-1]=='{':
                stack.pop()
            else:
                return False
    if stack==[]:
        return True
    else:
        return False

print(isValid(""))