# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        og_head = head
        while head.next != None:
            heads_next = head.next
            gcd = math.gcd(head.val, heads_next.val)
            head.next = ListNode(gcd, heads_next)
            head = heads_next
        return og_head
