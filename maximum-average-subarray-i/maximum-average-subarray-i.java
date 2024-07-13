class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double curr = 0;
        
        
        for (int right = 0; right < k; right ++){
            curr += nums[right];
        }
        double ans = curr;
        for (int i = k; i < nums.length; i ++){
            curr += nums[i] - nums[i-k];
            
            ans = Math.max(ans, curr);
        }
        
        return ans /k;
        
    }
}