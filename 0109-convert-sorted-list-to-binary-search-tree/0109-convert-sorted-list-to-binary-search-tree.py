# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return 
        
        if not head.next:
            return TreeNode(head.val)
        
        fast = head
        mid = head
        while fast and fast.next:
            prev = mid
            fast = fast.next.next
            mid = mid.next
        
        prev.next = None
        next_half = mid.next

        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(next_half)

        return root
