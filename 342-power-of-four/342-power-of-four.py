import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n >= 1:
            x = math.log(n, 4) 
            return 4 ** int(x) == n