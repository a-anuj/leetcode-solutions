class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort()
        capacity.reverse()
        count=0

        for i in range(len(capacity)):
            total_apples = total_apples-capacity[i]
            count+=1
            if total_apples<=0:
                return count
        