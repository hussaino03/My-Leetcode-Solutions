class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        result = a + b
        get_bin = lambda x: format(x, 'b')
        return get_bin(result)