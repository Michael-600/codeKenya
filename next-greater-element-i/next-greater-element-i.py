class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        ans = []
        
        for num in nums2:
            while (stack and num > stack[-1]):
                dic[stack.pop()] = num
                
            stack.append(num)
        
        
        
        while stack:
            dic[stack.pop()] = -1
        
        for c in nums1:
            ans.append(dic[c])
        
        return ans
            
            
        
        
        