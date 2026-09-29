# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left, right = -float('inf'), float('inf')
        def isValid(node, left, right):
            if not node:
                return True

            if not(node.val > left and node.val < right):
                return False

            p1 = isValid(node.left, left, node.val)
            p2 = isValid(node.right, node.val, right)
            return p1 and p2

        return isValid(root, left, right)
        