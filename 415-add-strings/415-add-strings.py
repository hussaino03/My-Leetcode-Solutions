class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        x, y = len(num1) -1, len(num2) -1
        lst, carry = [], 0
        
        while x >= 0 or y >= 0:
            if x >= 0:
                a = int(num1[x])
            else:
                a = 0
            if y >= 0:
                b = int(num2[y])
            else:
                b = 0
                
            curr = a + b + carry
            
            carried_over = str(curr % 10)
            
            lst.append(carried_over)
            
            carry = curr // 10
            
            x -= 1
            y -= 1
            
        if carry != 0:
            lst.append(str(carry))
        
        lst.reverse()
        return "".join(lst)
                
            
            
        
        
        
        