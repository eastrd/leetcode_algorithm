class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.best = 0
        
        def dfs(node):
            if not node:
                return 0
            l_s, r_s = dfs(node.left), dfs(node.right)
            l, r = l_s + 1 if node.left and node.left.val == node.val else 0, r_s + 1 if node.right and node.right.val == node.val else 0
            self.best = max(self.best, l + r)
            return max(l, r)
           
        dfs(root)
        return self.best
