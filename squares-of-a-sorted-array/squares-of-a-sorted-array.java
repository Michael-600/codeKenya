class Solution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        int[] new_nums = new int[n];
        
        for (int i = n - 1; i >= 0; i--){
            if(Math.abs(nums[left]) < Math.abs(nums[right])){
                new_nums[i] = nums[right];
                right --;
            }else{
                new_nums[i] = nums[left];
                left ++;
            }
            
            new_nums[i] = new_nums[i] * new_nums[i];
             
        }
               
        return new_nums;
        
        
        
    }
}