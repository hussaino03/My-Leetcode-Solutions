class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        a = 1
        nums.sort()
        if a in nums:
            for i in range(len(nums)):
                c = nums[i]
                if c == a:
                    a += 1       
        return a