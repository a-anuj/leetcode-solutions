# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def pre(node,res):
            if not node:
                return res
            res.append(node.val)
            pre(node.left,res)
            pre(node.right,res)
            return res

        resarray = pre(root,[])

        seen = {}
        for i in range(len(resarray)):
            diff = k - resarray[i]
            if diff in seen:
                return True
            seen[resarray[i]] = i
        return False