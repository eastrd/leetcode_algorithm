class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return lists
        if len(lists) < 2:
            return lists[0]
        res = []
        for i in lists:
            while i:
                res.append(i)
                i = i.next
        
        
        res = sorted(res, key=lambda x: x.val)
        head = node = ListNode(None)
        for i in res:
            node.next = i
            node = i
        return head.next
