# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        stack = [[root]]
        ans = []
        while stack[0]:
            levelVals , nextLevel = [] ,[]
            levelNodes = stack.pop()
            for x in levelNodes:
                levelVals.append(x.val)
                if x.left:
                    nextLevel.append(x.left)
                if x.right:
                    nextLevel.append(x.right)
            ans.append(levelVals)
            stack.append(nextLevel)
        return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s = Solution()
print(s.levelOrder(root))