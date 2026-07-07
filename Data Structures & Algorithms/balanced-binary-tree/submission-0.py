# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0
            return 1 + max(dfs(root.right), dfs(root.left))
        if root is None:
            return True
        leftLen = dfs(root.left)
        rightLen = dfs(root.right)

        if abs(leftLen - rightLen) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        