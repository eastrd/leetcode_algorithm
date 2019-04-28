# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return False
        if node == p or node == q:
            return node
        l, r = self.lowestCommonAncestor(node.left, p, q), self.lowestCommonAncestor(node.right, p, q)
        if not r:
            return l
        if not l:
            return r
        return node
