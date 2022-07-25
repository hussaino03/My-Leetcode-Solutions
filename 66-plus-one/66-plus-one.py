class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = [str(i) for i in digits]        
        s2 = "".join(s)                    
										
        z = int(s2) + 1                    
        answer =[x for x in str(z)]         

        return answer
    
    