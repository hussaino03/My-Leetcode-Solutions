class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)) : 
            num1 = nums[i]
            if (target - num1) in nums[i+1:] : 
                return [i, (nums[i+1:].index((target - num1)))+i+1]