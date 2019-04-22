"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        current = head
        node_dict = {None:None}
        root = copy = Node(None, None, None)
        while current:
            node = Node(current.val, None, current.random)
            # print(id(current), current.val)
            node_dict[id(current)] = node
            copy.next = node
            copy = node
            current = current.next
        # print(node_dict)
        # Build random
        current = root
        while current:
            # print(current.val, id(current.random))
            current.random = node_dict[id(current.random)] if id(current.random) in node_dict else None
            current = current.next
            
        return root.next
