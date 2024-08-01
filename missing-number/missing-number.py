class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()
        expected = len(nums) + 1
        ans = 0
        
        for i in nums:
            if i not  in seen:
                seen.add(i)
                
        print(seen)
                
        for i in range(expected):
            if i not in seen:
                ans = i 
                
        return ans
                
            
                
    
        