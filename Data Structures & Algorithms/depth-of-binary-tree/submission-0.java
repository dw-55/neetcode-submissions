/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int depth = 0;
        int current = 1;

        if (root == null) {
            return 0;
        }

        // while (!queue.isEmpty()) {
        //     TreeNode current = queue.poll();

        //     if (current.left != null) {
        //         queue.add(current.left);
        //     }

        //     if (current.right != null) {
        //         queue.add(current.right);
        //     }
        // }
    
        // depth = Math.max(current, depth)
        // if (root == null) [
        //     return 1;
        // ]
        // depth = Math.max(maxDepth(root.left), depth);
        // maxDepth(root.right);
        return dfs(root, depth);

    }

    public int dfs(TreeNode node, Integer current) {
        int depth = 0;
        if (node == null) {
            return current;
        }
        // dfs(node.left, current+1);
        depth = Math.max(dfs(node.left, current+1), depth);
        // dfs(node.right, current+1);
        depth = Math.max(dfs(node.right, current+1), depth);

        return depth;
    }
}
