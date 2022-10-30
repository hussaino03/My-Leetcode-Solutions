class Solution {
    public boolean isPrefixString(String s, String[] words) {
        String d = "";
        
        for(String i: words){
            d += i;
            if(d.equals(s)){
                return true;
            }else{
                continue;
            }
        }
        return false;
    }
}