# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = [[root]]
        level = 0
        while stack[0]:
            level += 1
            nextLevel = []
            levelNodes = stack.pop()
            for x in levelNodes:
                if x.left:
                    nextLevel.append(x.left)
                if x.right:
                    nextLevel.append(x.right)
            stack.append(nextLevel)
        return level