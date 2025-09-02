class Solution(object):
    def productExceptSelf(self, nums):
        prefixarr = [1]
        suffixarr = [1] * len(nums)
        answer = []
        runningProduct = 1
        for i in range(1,len(nums)):
            runningProduct = runningProduct * nums[i-1]
            prefixarr.append(runningProduct)
        runningProduct = 1
        for i in range(len(nums)-2,-1,-1):
            runningProduct = runningProduct * nums[i+1]
            suffixarr[i] = runningProduct

        #suffix = [24,12,4,1]
        #prefix = [1,1,2,6]

        for i in range(len(prefixarr)):
            answer.append(prefixarr[i] * suffixarr[i])
        return answer
