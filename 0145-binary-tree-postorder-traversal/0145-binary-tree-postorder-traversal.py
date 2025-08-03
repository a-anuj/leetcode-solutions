# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                result.append(node.val)
            return result
        return helper(root)
                
        