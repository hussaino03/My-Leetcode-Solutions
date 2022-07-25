class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2:
            return max(nums)
        else:
            return sorted(set(nums))[-3] # since set removes duplicates