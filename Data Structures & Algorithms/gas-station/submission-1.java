class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int fuelUsage = 0;
        int fuelNeeded = 0;
        int[] fuelDifference = new int[cost.length];
        for (int i = 0; i < gas.length; i++) {
            fuelUsage += gas[i];
            fuelNeeded += cost[i];
            fuelDifference[i] = gas[i]-cost[i];
        }
        int curr = 0;
        if (fuelUsage < fuelNeeded) {
            return -1;
        }
        for (int next = 1; next < gas.length; next++) {
            if (fuelDifference[curr] < 0) {
                curr++;
            } else if (fuelDifference[curr] + fuelDifference[next] < 0) {
                curr = next;
            }
        }

        return curr;
    }
}
