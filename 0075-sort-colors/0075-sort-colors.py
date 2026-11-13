class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left = 0
        ptr = 0
        right = n-1

        while ptr <= right:
            if nums[ptr] == 0:
                nums[ptr],nums[left] = nums[left],nums[ptr]
                ptr += 1
                left += 1
            elif nums[ptr] == 1:
                ptr += 1
            else:
                nums[ptr],nums[right] = nums[right],nums[ptr]
                right -= 1
            
            