class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        left = ans = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            
            while counts[s[right]] > 1:
                if s[left] in counts:
                    counts[s[left]] -= 1
                
                left += 1
                
            ans = max(ans, right - left + 1)
        
        return ans 
        
        