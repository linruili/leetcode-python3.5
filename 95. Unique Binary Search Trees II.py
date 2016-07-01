# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def recursion(l,r):
            ans = []
            if l>r:
                ans.append(None)
                return ans
            for i in range(l,r+1):
                lb = recursion(l, i-1)
                rb = recursion(i+1 , r)
                for lc in lb:
                    for rc in rb:
                        root = TreeNode(i)
                        root.left , root.right = lc , rc
                        ans.append(root)
            return ans
        if n==0:
            return []
        return recursion(1,n)


