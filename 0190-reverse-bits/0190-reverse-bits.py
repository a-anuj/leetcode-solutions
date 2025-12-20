class Solution:
    def reverseBits(self, n: int) -> int:
        n = format(n,'032b')
        n = list(n)
        n.reverse()
        n = "".join(n)
        return int(n,2)
