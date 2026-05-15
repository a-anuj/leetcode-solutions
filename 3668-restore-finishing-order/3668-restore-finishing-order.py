class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        temp = []
        for i in order:
            if i in friends:
                temp.append(i)
        return temp