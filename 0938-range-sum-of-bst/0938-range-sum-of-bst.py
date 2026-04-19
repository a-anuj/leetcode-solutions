# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def PreOrderTraversal(node,sumval):
            if not node:
                return sumval
            
            if low<=node.val<=high:
                sumval+=node.val
            sumval = PreOrderTraversal(node.left,sumval)
            sumval = PreOrderTraversal(node.right,sumval)
            return sumval
        
        ans = PreOrderTraversal(root,0)
        return ans