class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length-1;
        int mid;
        int minimum = Integer.MAX_VALUE;
        if (nums[low] < nums[high]) {
            return nums[low];
        }

        while (low <= high) {
            mid = low + (high-low)/2;
            if (nums[mid] <= nums[high]) {
                minimum = Math.min(nums[mid], minimum);
                high = mid - 1;
            } else if (nums[mid] > nums[high]){
                minimum = Math.min(nums[mid], minimum);
                low = mid + 1;
            }
        }

        return minimum;
    }
}
