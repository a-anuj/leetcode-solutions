class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        map1 = {0:1}
        count = 0

        for num in nums:
            prefixSum += num

            if prefixSum-k in map1:
                count += map1[prefixSum-k]

            map1[prefixSum] =  map1.get(prefixSum,0)+1
        return count