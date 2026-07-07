class Solution {
    public boolean isNStraightHand(int[] hand, int groupSize) {
        Map<Integer, Integer> map = new HashMap<>();
        if (hand.length % groupSize != 0) {
            return false;
        }
        Arrays.sort(hand);
        for (int i = 0; i < hand.length; i++) {
            if (map.containsKey(hand[i])) {
                map.put(hand[i], map.get(hand[i]) + 1);
            } else {
                map.put(hand[i], 1);
            }
        }
        for (int card : hand) {
            if (map.get(card) == 0) {
                continue;
            }

            for (int i = 0; i < groupSize; i++) {
                int nextCard = card + i;
                if (!map.containsKey(nextCard) || map.get(nextCard) == 0) {
                    return false;
                }
                map.put(nextCard, map.get(nextCard) - 1);
            }
        }

        return true;

    }
}
