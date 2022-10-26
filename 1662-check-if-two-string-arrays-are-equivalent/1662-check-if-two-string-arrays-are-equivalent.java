class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        String s = "";
        String c = "";
        for (String i: word1){
            s += i;
       }
        for (String d: word2){
            c += d;
        }
        return s.equals(c);
    }
    
}