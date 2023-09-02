# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        store = []
        cur = head
        n = 0
        while cur != None:
            store.append(cur.val)
            n += 1
            cur = cur.next
        return max(list(map( lambda n1, n2 : n1+n2, store[:n//2], store[::-1][:n//2])))