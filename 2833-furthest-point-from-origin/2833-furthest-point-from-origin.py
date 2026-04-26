class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        moves_list = list(moves)
        dictio = {}
        for i in moves_list : 
            dictio[i] = dictio.get(i,0) + 1
        lst = [i for i in dictio.values()]
        lst.sort(reverse=True)
        if len(lst)==3:
            return lst[0]+lst[1]-lst[2]
        elif len(lst) == 2:
            if "L" in dictio and "R" in dictio:
                return lst[0] - lst[1]
            else:
                return lst[0]+lst[1]
        else:
            return lst[0]