class Solution:
    def isValid(self, s: str) -> bool:
        store = {"(":")","[":"]","{":"}"}

        stack = []
        opening = "({["

        for sym in s:
            if sym in opening:
                stack.append(sym)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if store[val] != sym:
                    return False
        if not stack:
            return True
        else:
            return False
        