class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        mini = []
        for x in d.values():
            mini.append(x)
            
        minimum = min(mini)
        
        for key, value in d.items():
            if value == minimum:
                return key
            