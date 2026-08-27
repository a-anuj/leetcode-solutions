import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        result = ""
        heap = []
        for char,count in freq.items():
            heapq.heappush(heap, (-count,char))

        while len(heap)>=2:
            count_1,char_1 = heapq.heappop(heap)
            count_2,char_2 = heapq.heappop(heap)

            result+=char_1
            result+=char_2

            count_1 += 1
            count_2 += 1

            if count_1 < 0:
                heapq.heappush(heap,(count_1,char_1))
            if count_2 < 0:
                heapq.heappush(heap,(count_2,char_2))
            
        if heap:
            count,char = heapq.heappop(heap)
            if count <-1:
                return ""
            result += char
        return result