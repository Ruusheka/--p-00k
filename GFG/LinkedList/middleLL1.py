'''
structure of a linked list node 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        
        nn=Node(x)
        
        if head is None:
            return nn
        
        slow=head
        fast=head
        
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        nn.next=slow.next
        slow.next=nn
        
        return head