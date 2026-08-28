from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = defaultdict(set)

        for row,seat in reservedSeats:
            reserved[row].add(seat)
        
        result = (n-len(reserved)) * 2

        for row in reserved:
            seats = reserved[row]

            left = all(seat not in seats for seat in range(2,6))
            middle = all(seat not in seats for seat in range(4,8))
            right = all(seat not in seats for seat in range(6,10))

            if left and right:
                result += 2
            elif left or right or middle:
                result += 1
        return result