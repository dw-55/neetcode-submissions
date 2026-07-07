class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = nums[0]
        min = 1
        boundary = nums[0]
        if (len(nums) == 1):
            return 0
        if (len(nums) == 2):
            return 1
        for i in range(len(nums)):
            if (i > boundary):
                min += 1
                boundary = farthest
            if (i <= farthest):
                farthest = max(farthest, i+nums[i])
                
        return min