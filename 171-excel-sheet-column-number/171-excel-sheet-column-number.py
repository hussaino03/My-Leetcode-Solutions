class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum(list((26 ** (len(columnTitle) - i - 1)) * (ord(columnTitle[i]) - 64) for i in range(len(columnTitle))))