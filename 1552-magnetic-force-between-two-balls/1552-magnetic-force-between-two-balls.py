class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlace(num,m):
            last = position[0]
            m -= 1

            for i in range(1,len(position)):
                if position[i] - last >= num:
                    m -= 1
                    last = position[i]
                if m == 0:
                    return True
            return False

        low = 1
        high = position[-1] - position[0]
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if canPlace(mid,m):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans