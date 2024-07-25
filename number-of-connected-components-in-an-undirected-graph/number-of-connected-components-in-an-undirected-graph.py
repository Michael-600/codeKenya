class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        graph = defaultdict(list)
        ans = 0
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
            
        return ans
                    
        
                    
        