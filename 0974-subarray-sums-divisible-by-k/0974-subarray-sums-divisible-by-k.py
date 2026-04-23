class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        freq = {0:1}
        count=0
        for num in nums:
            prefix+=num
            rem = prefix%k
            count += freq.get(rem,0)
            freq[rem] = freq.get(rem,0)+1
        return count