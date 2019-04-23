# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(node):
            if not node:
                return
            if not node.next:
                return node
            pre, node = node, node.next
            next = node.next
            node.next, pre.next = pre, next
            pre.next = swap(pre.next)
            return node
        
        return swap(head)
