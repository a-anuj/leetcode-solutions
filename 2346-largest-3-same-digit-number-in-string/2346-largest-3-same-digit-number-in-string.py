class Solution(object):
    def largestGoodInteger(self, num):
        # maxval = 0
        # number = 0
        # for i in num:
        #     if (num.count(i)>=3) and ((i*3) in num):
        #         number = i*3
        #     maxval = max(maxval,number)
        # return "" if str(maxval) == "0" else str(maxval)

        # Another approach

        for i in range(9,-1,-1):
            substring = str(i) * 3
            if substring in num:
                return substring
        return ""
        