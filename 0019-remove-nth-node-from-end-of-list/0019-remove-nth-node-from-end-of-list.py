# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        totLength = 0
        while curr:
            totLength += 1
            curr = curr.next
        
        if totLength == 1:
            return None

        counter = 2
        curr = head
        while counter<totLength-n+1:
            curr = curr.next
            counter += 1
        if totLength-n+1 == 1:
            return curr.next
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return head


        

