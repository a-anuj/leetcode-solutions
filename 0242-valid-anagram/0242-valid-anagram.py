from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        # lstS = list(s)
        # lstT = list(t)

        # for i in lstT:
        #     if i in lstS:
        #         lstS.remove(i)
        #     else:
        #         return False
        # return len(lstS)==0

        return Counter(s) == Counter(t)