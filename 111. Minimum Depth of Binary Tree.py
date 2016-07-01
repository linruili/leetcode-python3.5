# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = [[root]]
        level = 1
        while stack[0]:
            nextLevel = []
            levelNodes = stack.pop()
            for x in levelNodes:
                if not x.left and not x.right:
                    return level
                if x.left:
                    nextLevel.append(x.left)
                if x.right:
                    nextLevel.append(x.right)
            level += 1
            stack.append(nextLevel)