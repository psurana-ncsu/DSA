"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        while curr:
            # if child exist, add that to the next
            if curr.child:
                temp=curr
                store=temp.next
                temp.next=temp.child
                temp.next.prev=temp
                temp.child=None
                
                #traverse untill the end of curr list of nodes
                while temp.next:
                    temp=temp.next
                temp.next=store
                if store:
                    temp.next.prev=temp
            curr=curr.next
        return head
