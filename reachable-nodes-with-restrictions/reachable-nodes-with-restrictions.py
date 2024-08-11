class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen and neighbour not in restricted:
                    seen.add(neighbour)
                    dfs(neighbour)
        
        restricted = set(restricted)
        seen = set()
        graph = defaultdict(list)
        
       
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen.add(0)
        dfs(0)
        
        return len(seen)
                
            
            
            
        