# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=deque([root])
        res = []
        
        while queue:
            queueLen = len(queue)
            level= []
            for i in range(queueLen):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            if level:
                rightMost = level.pop()
                res.append(rightMost)
            
        return res