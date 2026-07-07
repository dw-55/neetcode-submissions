class Solution {
    public int lengthOfLongestSubstring(String s) {
        Queue<Character> queue = new ArrayDeque<>();
        int maximum = 0;
        int length = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (queue.contains(c)) {
                while (queue.contains(s.charAt(i))) {
                    queue.remove();
                    length--;
                }
            }            
            queue.add(c);
            length++;
            maximum = Math.max(length,maximum);
        }

        return maximum;
    }
}
