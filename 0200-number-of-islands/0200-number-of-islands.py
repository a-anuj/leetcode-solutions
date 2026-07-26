class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        

        visited = set()
        count = 0

        def bfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return
            visited.add((r,c))
            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)

        for i in range(rows):
            for j in range(cols):   
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    bfs(i,j)
        return count