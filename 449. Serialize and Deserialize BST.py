# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack = []
        while True:
            while root:
                res.append(str(root.val))
                stack.append(root)
                root = root.left
            if not stack:
                return " ".join(res)
            node = stack.pop()
            root = node.right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        res = data.split(" ")
        head = root = TreeNode(int(res.pop(0)))
        def construct(head, node):
            while True:
                if node.val > head.val:
                    if head.right:
                        head = head.right
                    else:
                        head.right = node
                        break
                if node.val < head.val:
                    if head.left:
                        head = head.left
                    else:
                        head.left = node
                        break
        for v in res:
            construct(root, TreeNode(int(v)))
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
