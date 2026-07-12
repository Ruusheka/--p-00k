'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
'''        

class Solution:
    def cloneLinkedList(self, head):
        # code here
        if not head:
            return None
        
        curr=head
        while curr:
            copy=Node(curr.data)
            copy.next=curr.next
            curr.next=copy
            curr=copy.next
            
        
        curr=head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr=curr.next.next
        
        
        curr=head
        clone_head = head.next
        
        while curr:
            copy=curr.next
            curr.next=copy.next
            
            if copy.next:
                copy.next = copy.next.next
                
            curr = curr.next
            
        
        return clone_head