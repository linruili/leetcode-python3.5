# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            ans.append(root.val)
            recursion(root.right)

        ans = []
        recursion(root)
        return ans
