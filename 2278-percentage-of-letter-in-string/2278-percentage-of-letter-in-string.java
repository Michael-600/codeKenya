class Solution {
    public int percentageLetter(String s, char letter) {
        int len = s.length();
        int count = 0;
        
        
        for (int i = 0; i < len; i ++){
                if (s.charAt(i) == letter){
                    count ++;
                }
        }
        
        double len2 = len;
        double count2 = count;
        
        double ans =  count2 / len2 * 100;
        int ans2 = (int) ans;
        return ans2;
    }
}