class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        Map<Character, Integer> count = new HashMap<>();
        int left = 0;
        int max = 0;
        
        for (int right = 0; right < n; right ++){
            char c = s.charAt(right);
            count.put(c, count.getOrDefault(c, 0) + 1);
            while (count.get(c) >= 2){
                char remove = s.charAt(left);
                count.put(remove, count.getOrDefault(remove, 0) - 1);
                if (count.get(remove) == 0 ){
                    count.remove(remove);
                }
                left ++;
            
            }
            max = Math.max(max, right - left + 1);
        }
        return max;
    }
}