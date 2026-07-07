class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [None] * len(nums)
        leftProduct = 1
        rightProduct = 1
        prev = [None] * len(nums)
        prev[0] = 1

        for i in range(1, len(nums)):
            leftProduct *= nums[i-1]
            prev[i] = leftProduct
        
        for j in range(len(nums)-1, -1, -1):
            result[j] = prev[j] * rightProduct
            rightProduct *= nums[j]

        return result