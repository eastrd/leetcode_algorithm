# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, x):
            if not node:
                return []
            if node == x:
                return [node]
            l, r = find_path(node.left, x), find_path(node.right, x)
            if l:
                return [node] + l
            if r:
                return [node] + r
            return []
        path_p, path_q = deque(find_path(root, p)), deque(find_path(root, q))
        lowest = None
        while path_p and path_q:
            a, b = path_p.popleft(), path_q.popleft()
            if a == b:
                lowest = a
        return lowest
