class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = ans = curr = 0
        
        for i in range(k):
            curr += nums[i]
            
        ans = curr/k 
        
        for right in range(k, len(nums)):
            curr +=  nums[right] - nums[right - k ] 
            ans = max(ans, curr/k)
            
        return ans
            
            
        