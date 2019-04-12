class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, lower, upper):
            # Check current node is less than left & larger than right
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
            
        lower, upper = -float("inf"), float("inf")
        return dfs(root, lower, upper)
