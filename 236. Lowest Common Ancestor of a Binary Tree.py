# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def path_to_x(node, x):
            if not node:
                return None
            if node == x:
                return [node]
            left, right = path_to_x(node.left, x), path_to_x(node.right, x)
            if left:
                return [node] + left
            if right:
                return [node] + right
            return None
        path_to_p = path_to_x(root, p)
        path_to_q = path_to_x(root, q)
        
        lowest = None
        while path_to_p and path_to_q:
            a, b = path_to_p.pop(0), path_to_q.pop(0)
            if a == b:
                lowest = a
            else:
                break
        return lowest
