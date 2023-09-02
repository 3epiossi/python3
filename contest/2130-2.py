 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        testBound, cur = head, head
        prev = None
        while testBound != None and testBound.next != None:
            testBound = testBound.next.next #記得讓它先跑, 否則會被後面切斷

            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        res = -math.inf
        while prev != None:
            res = max(res, prev.val+cur.val)
            prev = prev.next
            cur = cur.next
        return res