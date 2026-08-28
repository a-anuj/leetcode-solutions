class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        ptr = 0
        right = len(nums) - 1

        while ptr <= right:
            if nums[ptr] == 0:
                nums[ptr],nums[left] = nums[left],nums[ptr]
                ptr += 1
                left += 1
            
            elif nums[ptr] == 1:
                ptr+=1
            
            elif nums[ptr] == 2:
                nums[ptr],nums[right] = nums[right],nums[ptr]
                right -= 1

        return nums