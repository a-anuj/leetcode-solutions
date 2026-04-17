# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def preOrderTraversal(node,result):
            if not node:
                return result
            
            result.append(node.val)
            preOrderTraversal(node.left,result)
            preOrderTraversal(node.right,result)

            return result
        
        result = preOrderTraversal(root,[])
        return len(result)