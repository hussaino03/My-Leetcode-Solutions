class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for item in nums:
            if item not in d:
                d[item] = 0
            if item in d:
                d[item] += 1
        for num in d:
            if d[num] >= 2:
                return d[num]
