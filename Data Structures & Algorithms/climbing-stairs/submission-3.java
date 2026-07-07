class Solution {
    int[] array;
    public int climbStairs(int n) {
        array = new int[n+1];
        array[0] = 1;
        array[1] = 1;
        return dp(n);
    }
    public int dp(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (array[n] > 0) {
            return array[n];
        } else {
            array[n] = dp(n - 1) + dp(n - 2);
        }
        return array[n];
    }
}
