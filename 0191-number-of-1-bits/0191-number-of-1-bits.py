class Solution(object):
    def hammingWeight(self, n):
        count = 0

        while(n>0):
            temp = n%2
            if temp==1:
                count+=1
            n/=2
        return count
        