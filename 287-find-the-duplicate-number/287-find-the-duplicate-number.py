class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    
    #slow yet correct solution:
    
#         new = []
#         for i in nums:
#             i = str(i)
#             new.append(i)
        
#         for a in new:
#             if new.count(a) > 1:
#                 return a