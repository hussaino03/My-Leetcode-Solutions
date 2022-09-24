class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        i = 1
        while i <= n:
            lst.append(str(i))
            i += 1
            
        for i in range(len(lst)):
            lst[i] = int(lst[i])
            if lst[i] % 3 == 0 and lst[i] % 5 == 0:
                lst[i] = "FizzBuzz"
                
            elif lst[i] % 3 == 0:
                lst[i] = "Fizz"
                
            elif lst[i] % 5 == 0:
                lst[i] = "Buzz"
                
        return [str(x) for x in lst]
                
            
