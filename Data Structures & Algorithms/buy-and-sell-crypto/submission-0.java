class Solution {
    public int maxProfit(int[] prices) {
        int max = 0;
        int i = 1;
        int buy = prices[i-1];
        int sell;

        while (i != prices.length) {
            sell = prices[i];
            if (prices[i] < buy) {
                buy = prices[i];
            }
            max = Math.max(sell - buy, max);
            i++;
        }

        return max;

    }
}
