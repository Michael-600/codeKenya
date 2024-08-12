class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        
        for x, y in points:
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            print(dist)
            heapq.heappush(heap, (-dist, -x, -y))
            if len(heap) > k:
                heapq.heappop(heap)
                
        print(heap)
        for x, i, j in heap:
            ans.append([-i, -j])
            
        return ans
            
        