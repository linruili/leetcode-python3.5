# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def recursion(root):
            if not root:
                return
            r = root.right
            if root.left:
                recursion(root.left)
                root.right = root.left
                root.left = None
                while root.right:
                    root = root.right
                root.right = r
            recursion(r)
        recursion(root)

