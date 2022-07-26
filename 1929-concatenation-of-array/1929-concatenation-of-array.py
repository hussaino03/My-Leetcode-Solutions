class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = []
        y =[]
        for s in nums:
            x.append(s)
            y.append(s)
            
        return x + y