class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        maxDiag = 0
        result = 0
        for i in dimensions:
            diagLength = ((i[0] * i[0]) + (i[1]*i[1]))**0.5
            if diagLength>maxDiag:
                maxDiag = diagLength
                result = i[0] * i[1]   
            elif diagLength == maxDiag:
                result = max(result,i[0]*i[1])
        return result
        