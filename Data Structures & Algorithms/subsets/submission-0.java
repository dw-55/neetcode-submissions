class Solution {
    List<List<Integer>> unique = new ArrayList<>();
    // List<Integer> subset = new ArrayList<>();
    public List<List<Integer>> subsets(int[] nums) {
        Arrays.sort(nums);
        allSubsets(0, nums, new ArrayList<>());
        return unique;
    }

    public void allSubsets(int n, int[] nums, List<Integer> subset) {
        unique.add(new ArrayList<>(subset));
        for (int i = n; i < nums.length; i++) {
            // if (i > n && nums[i]==nums[i-1]) {
            //     continue;
            // }
            subset.add(nums[i]);
            allSubsets(i+1,nums,subset);
            subset.remove(subset.size()-1);
        }
    }
}
