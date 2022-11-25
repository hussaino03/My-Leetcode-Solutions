class Solution {
    public boolean squareIsWhite(String coordinates) {
        String lett = coordinates.substring(0, 1);
        int num = Integer.parseInt(coordinates.substring(1));
        
        if (lett.equals("a") || lett.equals("c") || lett.equals("e") || lett.equals("g")){
            if (num % 2 == 0){
                return true;
            }else{
                return false;
            }
        }else{
            if (num % 2 == 0){
                return false;
            }else{
                return true;
            }
        }
        
    }
}
