class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<>();
        int maximum = 0;
        int length = 0;
        int front = 0;
        int back = 0;

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (set.contains(c)) {
                while (set.contains(c)) {
                    // s.remove(s.charAt(front));
                    set.remove(s.charAt(front));
                    front++;
                    length--;
                }
            }            
            set.add(c);
            length++;
            maximum = Math.max(length,maximum);
        }

        return maximum;
    }
}
