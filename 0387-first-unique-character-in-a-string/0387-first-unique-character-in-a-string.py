from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for i in s:
            count[i] += 1
        for index,key in enumerate(s):
            if count[key] == 1:
                return index
        return -1
        