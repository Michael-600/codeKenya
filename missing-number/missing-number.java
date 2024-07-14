class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> mySet = new HashSet<>();
        
        for (int i = 0; i < nums.length; i ++){
            if (!mySet.contains(nums[i])){
                mySet.add(nums[i]);
            }
        }
        
        int expectedNum = nums.length + 1;
        for (int i = 0; i < expectedNum; i ++){
            if (!mySet.contains(i)){
                return i;
            }
        }
        return -1;
    
        
    }
}