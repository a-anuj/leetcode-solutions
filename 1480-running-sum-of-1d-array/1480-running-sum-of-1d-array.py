class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp = [nums[0]]
        for i in range(1,len(nums)):
            temp.append(temp[i-1]+nums[i])
        return temp