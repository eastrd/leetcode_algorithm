# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:    
    def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        
        if not root:
            return []
        
        res = []
        
        def dfs(node, layer):
            if not node:
                return
            # Check if layer index exists in res
            if len(res) < layer + 1:
                res.append([])
            res[layer].append(node.val)
            dfs(node.left, layer+1)
            dfs(node.right, layer+1)

        dfs(root, 0)

        # Reverse every second result
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]

        return res
