class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalTank = 0;
        int currTank = 0;
        int startIndex = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            totalTank += diff;
            currTank += diff;
            if (currTank < 0) {
                startIndex = i+1;
                currTank = 0;
            }
        }
        if (totalTank < 0) {
            return -1;
        } 
        return startIndex;
    }
}
