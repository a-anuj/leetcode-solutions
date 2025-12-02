class Solution(object):
    def findWords(self, words):
        answer = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        for w in words:
            s = set(w.lower())

            if s.issubset(row1) or s.issubset(row2) or s.issubset(row3):
                answer.append(w)
        return answer
            
