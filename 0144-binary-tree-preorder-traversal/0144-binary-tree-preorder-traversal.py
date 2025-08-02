# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = []
    def preorderTraversal(self, root):
        result = []
        def helper(root):
            if root:
                result.append(root.val)
                helper(root.left)
                helper(root.right)
            return result
        return helper(root)