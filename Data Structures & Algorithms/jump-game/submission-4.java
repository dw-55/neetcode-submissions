class Solution {
    public boolean canJump(int[] nums) {
        int farthest = nums[0];
        if (nums.length == 1) {
            return true;
        }
        if (nums[0] == 0) {
            return false;
        }
        for (int i = 1; i < nums.length; i++) {
            if (i <= farthest) {
                farthest = Math.max(farthest, i+nums[i]);
            }
            if (farthest >= nums.length - 1) {
                return true;
            }
        }
        return false;
    }
}
