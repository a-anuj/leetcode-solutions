class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_final = 0

        for num in nums:
            if num==1:
                count+=1
            else:
                count = 0
            count_final = max(count_final,count)
        return count_final