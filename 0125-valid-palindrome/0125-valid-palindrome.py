class Solution(object):
    def isPalindrome(self, s):
        temp = ""
        alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in s:
            if i.lower() in alpha:
                temp+=i.lower()
        
        reverse = temp[::-1]
        if reverse == temp:
            return True
        else:
            return False
        