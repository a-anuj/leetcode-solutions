# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        temp = []

        while head:
            temp.append(head.val)
            head = head.next
        
        result = 0
        length = len(temp)-1
        for i in temp:
            result += i*(2**length)
            length -= 1
        
        return result