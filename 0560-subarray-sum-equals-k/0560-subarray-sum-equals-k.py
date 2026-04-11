class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        mapCount = {0:1}
        count = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in mapCount:
                count += mapCount[prefixSum-k] 
            
            mapCount[prefixSum] = mapCount.get(prefixSum,0) + 1
        
        return count