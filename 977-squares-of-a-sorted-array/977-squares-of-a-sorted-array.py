class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             nums[i] = nums[i]**2
        
#         nums.sort()
#         return nums

# efficient solution
        temp = []
        L = 0
        R = len(nums) - 1
        while L <= R:
            if abs(nums[R]) > abs(nums[L]):
                temp.append(nums[R]**2)
                R -= 1
            else:
                temp.append(nums[L]**2)
                L += 1
        return temp[::-1]
            