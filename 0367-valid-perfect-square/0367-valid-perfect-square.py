class Solution(object):
    def isPerfectSquare(self, num):
        if num<2:
            return True
        
        left,right = 1,num
        while(left<=right):
            mid = (left+right)//2
            square = mid*mid

            if square == num:
                return True

            elif square>num:
                right = mid-1
            
            else:
                left = mid+1
        return False
            

        