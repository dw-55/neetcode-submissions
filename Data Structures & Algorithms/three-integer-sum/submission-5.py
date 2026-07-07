class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        left = 0
        result = []

        for integer in range (len(nums)-1):
            if len(nums)-integer <=2:
                return result
            left = integer + 1
            right = len(nums) - 1
            while left < right:
                if nums[left]+nums[right] < -nums[integer]:
                    left += 1
                elif nums[left]+nums[right] > -nums[integer]:
                    right -= 1
                else:
                    if [nums[left],nums[right],nums[integer]] in result:
                        left+= 1
                        continue
                    else:
                        result.append([nums[left],nums[right],nums[integer]])
                        right -= 1
            
        return result



