class Solution(object):
    def triangleType(self, nums):
        if len(nums) < 3 or len(nums)>3:
            return "none"
        
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[2] == nums[0]:
            if nums[0] +nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[2]+nums[0] > nums[1]:
                return "isosceles"
            else:
                return "none"
        
        else:
            if nums[0] +nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[2]+nums[0] > nums[1]:
                return "scalene"
            else:
                return "none"