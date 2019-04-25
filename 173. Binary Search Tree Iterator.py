# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        # Build the values as inorder traversal
        self.res = []
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return
            node = stack.pop()
            self.res.append(node.val)
            root = node.right

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.res.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not not self.res


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
