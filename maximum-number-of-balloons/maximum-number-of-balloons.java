class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> counts = new HashMap<>();
         int bCount = 0;
        int aCount = 0;
        int lCount = 0;
        int oCount = 0;
        int nCount = 0;
        
        for (int i = 0; i < text.length(); i ++){
            char c = text.charAt(i);
            counts.put(c, counts.getOrDefault(c, 0)+1);
        }
        
        if (counts.containsKey('b')){
            bCount = counts.get('b');
        }
        if (counts.containsKey('a')){
            aCount = counts.get('a');
        }
        if (counts.containsKey('l')){
            lCount = counts.get('l');
        }
        if (counts.containsKey('o')){
            oCount = counts.get('o');
        }
        if (counts.containsKey('n')){
            nCount = counts.get('n');
        }
        
        
        lCount = lCount/2;
        oCount = oCount/2;
        
        int results = Math.min(bCount, Math.min(aCount, Math.min(lCount, Math.min(oCount, nCount))));
        
        return results;
        
        
    }
}