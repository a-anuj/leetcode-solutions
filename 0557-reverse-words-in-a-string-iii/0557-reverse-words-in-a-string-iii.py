class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        temp = []

        for i in s:
            temp.append(i[::-1])

        final = ""

        for i in temp:
            final += i
            final += " "
        return final.strip()