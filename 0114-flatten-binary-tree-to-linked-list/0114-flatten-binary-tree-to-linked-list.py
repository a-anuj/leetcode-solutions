# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preOrderTraversal(node,result):
            if not node:
                return result
            
            result.append(node)
            preOrderTraversal(node.left,result)
            preOrderTraversal(node.right,result)
            return result
        
        result = preOrderTraversal(root,[])

        for i in range(len(result)-1):
            result[i].left = None
            result[i].right = result[i+1]




        