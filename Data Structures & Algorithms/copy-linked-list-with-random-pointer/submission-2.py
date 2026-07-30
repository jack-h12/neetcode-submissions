"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        copies = {}

        # this creates the dictionary with keys being the nodes, and values being a new version of the same node
        curr = head
        while curr is not None:
            copies[curr] = Node(curr.val)
            curr = curr.next

        # this adds in the .next and .random values to the newly created nodes
        curr = head
        while curr is not None:
            copies[curr].next = copies.get(curr.next)
            copies[curr].random = copies.get(curr.random)
            curr = curr.next
        
        return copies[head]


