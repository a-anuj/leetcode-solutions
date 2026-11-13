class Solution:
    def isValid(self, s: str) -> bool:
        store = {"(":")","[":"]","{":"}"}
        stack = []

        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                pair = stack.pop()
                if store[pair] != s[i]:
                    return False

        return True if not stack else False


