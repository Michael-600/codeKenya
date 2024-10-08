class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ptr1 = 0
        ptr2 = len(s) - 1
        
        while ptr1 < ptr2 :
            letter = s[ptr1]
            s[ptr1] = s[ptr2]
            s[ptr2] = letter
            
            ptr1 += 1
            ptr2 -= 1
        
        