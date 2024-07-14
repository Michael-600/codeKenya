class Solution {
    public int[] runningSum(int[] nums) {
        int[] prefix = new int[nums.length];
        prefix[0] = nums[0];
        
        System.out.println(prefix[0]);
        
        for (int i = 1; i < nums.length; i ++){
            prefix[i] = nums[i] + prefix[i - 1];
            System.out.println(prefix[i]);
        }
        
        return prefix;
        
    }
}