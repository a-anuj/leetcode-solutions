class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numarr = list(str(n))
        prod = 1
        sumv = 0
        for i in range(len(numarr)):
            numarr[i] = int(numarr[i])
            prod *= numarr[i]
            sumv += numarr[i]
        return prod-sumv