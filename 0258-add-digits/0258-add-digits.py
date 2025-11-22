class Solution(object):
    def addDigits(self, num):
        while True:
            result = 0
            digits = 1 if num==0 else int(math.log10(abs(num)))+1
            for i in range(digits):
                val = num%10
                result+=val
                num = num/10
            if result<10:
                return result
            else:
                num = result