from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            change = 0
            for _ in range(len(queue)):
                row,col = queue.popleft()
                
                if row+1<rows and grid[row+1][col] == 1:
                    fresh-=1
                    grid[row+1][col] = 2
                    queue.append((row+1,col))
                    change = 1
                    
                
                if row-1>=0 and grid[row-1][col] == 1:
                    fresh-=1
                    grid[row-1][col] = 2
                    queue.append((row-1,col))
                    change =1
                
                if col-1>=0 and grid[row][col-1] == 1:
                    fresh-=1
                    grid[row][col-1] = 2
                    queue.append((row,col-1))
                    change = 1

                if col+1<cols and grid[row][col+1] == 1:
                    fresh-=1
                    grid[row][col+1] = 2
                    queue.append((row,col+1))
                    change = 1
            if change:
                count += 1
        return count if fresh==0 else -1