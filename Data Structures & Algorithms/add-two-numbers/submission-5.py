# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2

        new_list_pre_head = ListNode()
        new_list_curr = new_list_pre_head

        carry = 0

        while l1_curr != None or l2_curr != None or carry != 0:
            if l1_curr != None:
                val1 = l1_curr.val
            else:
                val1 = 0
            
            if l2_curr != None:
                val2 = l2_curr.val
            else:
                val2 = 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10

            new_list_curr.next = ListNode(val)

            new_list_curr = new_list_curr.next
            if l1_curr != None:
                l1_curr = l1_curr.next
            else:
                l1_curr = None

            if l2_curr != None:
                l2_curr = l2_curr.next
            else:
                l2_curr = None            

        return new_list_pre_head.next

        
