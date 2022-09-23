class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int('-' + str(x)[:0:-1])

        if not (-2**31 <= res <= 2**31 - 1):
            return 0
        else:
            return res