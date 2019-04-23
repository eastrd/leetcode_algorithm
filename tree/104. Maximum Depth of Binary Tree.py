# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.rec = 0
        def traverse(node, depth):
            if not node:
                if depth > self.rec:
                    self.rec = depth
            else:
                traverse(node.left, depth+1)
                traverse(node.right, depth+1)
                
        traverse(root, 0)
        return self.rec
