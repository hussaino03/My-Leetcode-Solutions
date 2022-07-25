import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n >= 1:
            x = math.log(n, 2) 
            return 2**round(x) == n