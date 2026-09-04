class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            else:
                if target < nums[mid] or target >= nums[left]:
                    right = mid - 1
                elif target < nums[left] or target > nums[mid]:
                    left = mid + 1
                


            # if target > nums[mid] and target <= nums[right]:
            #     if target == nums[right]:
            #         return right
            #     left = mid + 1
            # elif target > nums[mid] and target > nums[right]:
            #     right = mid - 1
            # if target < nums[mid] and target >= nums[left]:
            #     if target == nums[left]:
            #         return left
            #     right = mid - 1
            # elif target < nums[mid] and target < nums[left]:
            #     if target == nums[left]:
            #         return left
            #     left = mid + 1

        return -1

            