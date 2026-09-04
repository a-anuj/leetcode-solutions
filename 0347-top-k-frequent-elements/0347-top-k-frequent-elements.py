from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for key,value in hashmap.items():
            bucket[value].append(key)
        
        ans = []
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                if k>0:
                    ans.append(j)
                    k-=1
        return ans

        



        