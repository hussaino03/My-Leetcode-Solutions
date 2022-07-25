import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n >= 1:
            x = math.log(n, 3)
            return 3**round(x) == n