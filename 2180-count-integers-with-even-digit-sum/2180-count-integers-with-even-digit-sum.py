class Solution:
    def countEven(self, num: int) -> int:
        return num // 2 if sum([int(x) for x in str(num)]) % 2 == 0 else (num - 1) // 2