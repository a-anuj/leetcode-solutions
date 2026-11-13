class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst = s.split(" ")
        result = []
        for i in range(len(lst)-1,0,-1):
            if not lst[i]:
                continue
            result.append(lst[i])
            
        result = " ".join(result)
        if len(lst) > 1:
            result+=" " + lst[0]
        else:
            result += lst[0]
        return result