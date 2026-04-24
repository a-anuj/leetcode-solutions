class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        if start_color == color:
            return image

        visited = set()

        rows = len(image)
        cols = len(image[0])

        def dfs(sr,sc):
            if sr<0 or sc<0 or sr>=rows or sc>=cols:
                return
            
            if image[sr][sc] != start_color:
                return

            if (sr,sc) in visited:
                return

            visited.add((sr,sc))
            image[sr][sc] = color
            
            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)
        
        dfs(sr,sc)
        return image