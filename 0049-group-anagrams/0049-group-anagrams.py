from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = defaultdict(list)
        for i in strs:
            key = "".join(sorted(i))
            store[key].append(i)
        return list(store.values())