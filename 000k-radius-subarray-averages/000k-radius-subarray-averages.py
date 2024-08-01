class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        results = [-1] * n 
        window = 2 * k + 1
        prefix = [nums[0]]

        for i in range(n):
            prefix.append(nums[i] + prefix[len(prefix) - 1])
        
        for i in range(k, n-k):
            leftbound = i - k
            rightbound = i + k
            sub = prefix[rightbound + 1] - prefix[leftbound]
            average = sub// window
            results[i] = average 
        
        return results
           
                
               
            
            
            
        
        
        