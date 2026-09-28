# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if root == p or root == q:
            return root

        p1 = self.lowestCommonAncestor(root.right, p ,q)
        p2 = self.lowestCommonAncestor(root.left, p, q)
    
        if p1 and p2:
            return root

        return p1 or p2