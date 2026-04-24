from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        def dijkstra(src,graph):
            dist = {i:float("inf") for i in range(1,n+1)}
            dist[src] = 0
            heap = [(0,src)]

            while heap:
                curr_dist, node = heapq.heappop(heap)
                for nei, weight in graph[node]:
                    new_dist = curr_dist + weight
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist
                        heapq.heappush(heap,(new_dist,nei))
            return dist

        dist = dijkstra(k,graph)
        if float("inf") in dist.values():
            return -1
        return max(dist.values())
        
