class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i,e in enumerate(nums):
            if e not in d:
                d[e] = 0
            if e in d:
                d[e] += 1
        for val in d:
            if d[val] > len(nums) / 2:
                return val
                
                
