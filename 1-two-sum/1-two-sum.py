class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            
            if nums[i] in res.keys():
                return[res[nums[i]],i]
            ans = target - nums[i]
            res[ans] = i