class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rev = s[:k]
        rev = rev[::-1]
        return rev + s[k:]