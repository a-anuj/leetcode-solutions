class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        

        while left<=right:
            dayVal = 1
            maxWeight = (left+right)//2
            curr_load = 0

            for w in weights:
                if curr_load + w <= maxWeight:
                    curr_load += w
                else :
                    dayVal+=1
                    curr_load = w
            
            if dayVal <= days:
                right = maxWeight-1
            else:
                left = maxWeight+1
        return left
