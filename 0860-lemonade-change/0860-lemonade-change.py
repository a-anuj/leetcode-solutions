class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        denominations = {"5":0,"10":0,"20":0}

        for bill in bills:
            denominations[str(bill)] += 1
            rem = bill-5
            if rem == 0:
                continue
            elif rem == 5:
                if denominations[str(rem)] < 1:
                    return False
                denominations[str(rem)] -= 1
            else:
                if denominations["10"] >= 1 and denominations["5"] >= 1:
                    denominations["10"]-=1
                    denominations["5"] -= 1
                else:
                    if denominations["5"] >= 3:
                        denominations["5"] -= 3
                    else:
                        return False


                    
                
        return True


