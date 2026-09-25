# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hashmap = {}
        for i in range(len(inorder)):
            self.hashmap[inorder[i]] = i

        # return self.dfs(preorder, inorder, 0)
        return self.dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
    
    # def dfs(self, preorder, inorder,in_offset):
    def dfs (self, preStart, preEnd, inStart, inEnd):
        # if not preorder or not inorder:
        if preStart > preEnd or inStart > inEnd:        
            return None

        root = TreeNode(preorder[preStart])
        # mid = hashmap.get(preorder[0])
        # mid = next(k for k, v in self.hashmap.items() if v == preorder[0]) - in_offset
        # mid = self.hashmap[preorder[0]] - in_offset
        mid = self.hashmap[preorder[preStart]]
        leftSize = mid - inStart
        root.left = self.dfs(preStart + 1, preStart + leftSize, inStart, mid - 1)
        root.right = self.dfs(preStart + leftSize + 1, preEnd, mid + 1, inEnd)
        return root