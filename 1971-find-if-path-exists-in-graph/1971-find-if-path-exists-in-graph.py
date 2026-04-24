from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        def dfs(graph,start,visited,result):
            if start not in visited:
                visited.add(start)
                result.append(start)
            
            for nei in graph[start]:
                if nei not in visited:
                    dfs(graph,nei,visited,result)
        
            return result
        
        result = dfs(graph, source, set(), [])
        if destination in result:
            return True
        else:
            return False


        