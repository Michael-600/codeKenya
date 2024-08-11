class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return  0 <= row < n and 0  <= col < m and grid[row][col] == 1
        
        def dfs(row, col):
            count = 1
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    count += dfs(next_row, next_col)
            return count 
            
        seen = set()
        maxx = 0
        directions = [(0,1), (1, 0), (0,-1), (-1,0)]
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in seen:
                    seen.add((i, j))
                    maxx = max(maxx, dfs(i, j))
                    
        return maxx
        
        
        