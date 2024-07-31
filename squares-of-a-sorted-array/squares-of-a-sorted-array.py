class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ptr1 = 0
        ptr2 = len(nums) - 1
        ptr3 = len(nums) - 1
        lst = [0] * len(nums)
        
        while ptr3 >= 0:
            if abs(nums[ptr1]) > abs(nums[ptr2]):
                lst[ptr3] = nums[ptr1] * nums[ptr1]
                ptr1 += 1
                ptr3 -= 1
            else:
                lst[ptr3] = nums[ptr2] * nums[ptr2]
                ptr2 -= 1
                ptr3 -= 1
                
        return lst
                
                
                
                
            
        