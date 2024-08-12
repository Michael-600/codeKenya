class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(heap)
        ans = 0
        
        while len(sticks) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            heapq.heappush(heap, first + second)
            ans += first + second
        
        return ans
            
        