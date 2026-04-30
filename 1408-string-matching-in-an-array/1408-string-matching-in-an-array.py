class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        lst = []
        for i in words:
            for j in words:
                if i in j and i!=j and i not in lst:
                    lst.append(i)
        return lst