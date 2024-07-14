class Solution {
    public boolean checkIfPangram(String sentence) {
        
        Set<Character> found = new HashSet<>();
        
        for (int i = 0; i < sentence.length(); i ++){
            char c = sentence.charAt(i);
            if (!found.contains(c)){
                found.add(c);
            }
        }
        
        return found.size() == 26;
        
    }
}