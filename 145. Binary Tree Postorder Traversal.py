# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            if not stack:
                return res[::-1]
            node = stack.pop()
            root = node.left
