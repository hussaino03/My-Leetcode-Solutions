class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1 = {}
    
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = i
            else:
                if abs(i-dict1[nums[i]]) <= k:
                    return True

                dict1[nums[i]] = i

        return False