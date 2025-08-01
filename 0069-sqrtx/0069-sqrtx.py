class Solution(object):
    def mySqrt(self, x):
        if(x<2):
            return x

        left = 1
        right = x

        while(left<=right):
            
            mid = (left+right)//2
            square = mid * mid

            if(square == x):
                return mid

            elif(square<x):
                left = mid+1

            else:
                right = mid-1

        return right
        