# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(r, max):
            if not r:
                return 0
            if r.val >= max:
                self.count += 1
                max = r.val
            
            dfs(r.left, max)
            dfs(r.right, max)
            # max = max(dfs(r.left), dfs(r.right))
        dfs(root, root.val)
        return self.count