class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        temp = []
        count = 0
        temp1 = nums.copy()
        for i in range(len(temp1)-1):
            temp.append(temp1[i])
            nums = temp1[i+1:]

            if (sum(temp)-sum(nums))%2==0:
                count+=1

        return count