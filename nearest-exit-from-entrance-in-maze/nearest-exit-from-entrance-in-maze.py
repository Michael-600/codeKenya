class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if maze[entrance[0]][entrance[1]] == "+":
            return -1
        
        
        def valid(row, col):
            return 0 <= row < n and  0 <= col < m and maze[row][col] == "."
            
            
        queue = deque([(entrance[0], entrance[1], 0)])
        seen = set((entrance[0], entrance[1]))
    
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        n = len(maze)
        m = len(maze[0])
        
        while queue:
            row, col, steps = queue.popleft()
            if (row != entrance[0] or col != entrance[1]) and (row == 0 or col == 0  or row == n - 1 or col == m - 1):
                return steps
            
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        
        return -1
            
        
        
        
        
        