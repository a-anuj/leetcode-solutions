class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while(n):
            if n%2 == 1 :
                count+=1
            n = n//2
        return count