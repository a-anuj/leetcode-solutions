class Solution(object):
    def check(self, nums):
        
        """ Brute Force
        if nums == sorted(nums):
            return True
        for i in range(1,len(nums)):
            if nums[i] == min(nums) and nums[i-1] == max(nums):
                temp_1 = nums[i:]
                temp_2 = nums[:i]
                temp_3 = temp_1 + temp_2
                if sorted(temp_1) == temp_1 and sorted(temp_2) == temp_2 and sorted(temp_3) == temp_3:
                    return True

        return False
        """

        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                count+=1
            if count>1:
                return False
        return True


