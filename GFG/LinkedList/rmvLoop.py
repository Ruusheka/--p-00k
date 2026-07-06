''' Structure of linked list Node
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        # code here
        if not head or not head.next:
            return
        
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                break
        
        else:
            return
        
        slow=head
        
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        
        while fast.next!=slow:
            fast=fast.next
        
        fast.next=None
        
        