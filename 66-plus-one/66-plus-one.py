class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            s1 = [str(i) for i in digits]        
            s2 = "".join(s1)                    
										
            add = int(s2) + 1                    
            output =[x for x in str(add)]         

            return output
    
    
 