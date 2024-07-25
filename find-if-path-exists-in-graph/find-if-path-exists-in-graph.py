class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        seen = set()
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            
        def dfs(curr_node):
            if curr_node == destination:
                return True

            for neighbour in graph[curr_node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    if dfs(neighbour):
                        return True

            return False 

        return dfs(source)
        
        
            
        
        
        