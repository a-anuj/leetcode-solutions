class Solution(object):
    def isValid(self, s):
        storage = {"(":")","{":"}","[":"]"}
        stack = []

        for i in s:
            if i in storage:
                stack.append(storage[i])
            else:
                if not stack or stack.pop() != i:
                    return False

        return not stack
        