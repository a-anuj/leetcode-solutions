class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = []
        count=0
        j=0
        for i in range(len(nums)):
            if nums[i]==0:
                j+=1
            else:
                break
        nums = nums[j:]
        for i in range(len(nums)):
            if nums[i] == 1 and i!=0:
                temp.append(count)
                count = 0
            elif nums[i]==0:
                count+=1

        for i in temp:
            if i<k:
                return False
        return True
        