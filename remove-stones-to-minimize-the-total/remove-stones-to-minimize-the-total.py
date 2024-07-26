class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        
        for i in range(k):
            x = heapq.heappop(heap)
            heapq.heappush(heap, x//2)
        
        newHeap= [-num for num in heap]
        return sum(newHeap)
        