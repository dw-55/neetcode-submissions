class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = nums[0]
        if (len(nums) == 1):
            return True
        if (nums[0] == 0):
            return False
        for i in range(len(nums)):
            if (i <= farthest):
                farthest = max(farthest, i+nums[i])
            
            if (farthest >= len(nums)-1):
                return True
        return False