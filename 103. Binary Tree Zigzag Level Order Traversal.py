# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack ,ans = [] , []
        if not root:
            return []
        stack.append(root)
        level = 0
        nodes = []
        while stack:
            next_level = []
            level += 1
            while stack:
                nodes.append(stack.pop())
            while nodes:
                node = nodes.pop(0)
                next_level.append(node.val)
                if level%2 ==1:
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)
                else:
                    if node.right:
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
            ans.append(next_level[:])
        return ans





