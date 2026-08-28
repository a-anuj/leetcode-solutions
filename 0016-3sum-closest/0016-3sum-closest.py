class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closer = float('inf')
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == target:
                    return target

                if abs(target-total) < abs(target-closer):
                    closer = total
                
                if total < target:
                    left += 1
                
                elif total > target:
                    right -= 1
        return closer
                


                