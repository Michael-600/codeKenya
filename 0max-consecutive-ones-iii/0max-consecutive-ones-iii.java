class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int curr = 0;
        int ans = 0;
        
        
        for (int right = 0; right < nums.length; right ++){
            if (nums[right] == 0){
                curr += 1;
            
            }
            while (curr > k){
                if (nums[left] == 0){
                    curr -= 1;
                }
                left ++;
                
            }
            ans = Math.max(ans, right - left + 1);
        
        }
        return ans;
    }
}