# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        arr = []
        while head:
            if head not in arr:
                arr.append(head)
                head=head.next
            else:
                return True
            
        