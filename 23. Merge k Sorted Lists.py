# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for ls in lists:
            while ls:
                res.append(ls.val)
                ls = ls.next
        res.sort()
        head = ListNode(None)
        cur = head
        for i in range(len(res)):
            node = ListNode(res[i])
            cur.next = node
            cur = cur.next
        return head.next
