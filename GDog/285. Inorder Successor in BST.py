# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p):
            if not node:
                return None
            self.dfs(node.left, p)
            if self.prev == p:
                self.succ = node
                self.prev = None
                return
            self.prev = node
            self.dfs(node.right, p)
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.prev = self.succ = None
        
        if root == p:
            return root.right
        self.dfs(root, p)
        return self.succ
