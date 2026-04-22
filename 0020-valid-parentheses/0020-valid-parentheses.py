class Solution:
    def isValid(self, s: str) -> bool:
        store = {"(":")","[":"]","{":"}"}

        stack = []
        opening = "([{"

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                val = stack.pop()
                if store.get(val) != s[i]:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
