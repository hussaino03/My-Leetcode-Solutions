
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
         counter = Counter(nums)
         res = 0
         for num in counter:
            if counter[num] == 1:
                res += num
         return res