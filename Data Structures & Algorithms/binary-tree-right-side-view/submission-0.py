# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        q = collections.deque([root])

        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
                
            if right:
                results.append(right.val)

        return results