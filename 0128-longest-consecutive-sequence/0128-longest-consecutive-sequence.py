class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maximum = 0
        nums = set(nums)
        for num in nums:
            if num-1 not in nums:
                temp = num
                count = 1

                while temp+1 in nums:
                    count += 1
                    temp+=1
                maximum = max(maximum,count)
        return maximum