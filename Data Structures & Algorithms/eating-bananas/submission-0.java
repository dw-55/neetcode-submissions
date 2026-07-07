class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        List<Integer> list = new ArrayList<>();
        if (h == piles.length) {
            return Arrays.stream(piles).max().getAsInt();
        }
        
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();
        int k;
        int hours = 0;

        while (low <= high) {
            k = low + (high - low)/2;
            for (int i = 0; i < piles.length; i++) {
                hours += (piles[i] + k - 1)/k;
            }
            
            if (hours > h) {
                low = k + 1;
            } else if (hours <= h) {
                high = k - 1;
                list.add(k);
            }
            hours = 0;
        }

        return Collections.min(list);
        
    }
}
