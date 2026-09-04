from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            sortval = "".join(sorted(strs[i]))
            hashmap[sortval].append(strs[i])
        return list(hashmap.values())