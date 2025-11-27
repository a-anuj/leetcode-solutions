# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        return temp==temp[::-1]