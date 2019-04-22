# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            root = node.right
        
