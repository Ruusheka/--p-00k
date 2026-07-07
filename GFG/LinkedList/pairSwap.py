"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        # code here
        if head is None or head.next is None:
            return head
            
        prev = None
        curr = head
        
        head = head.next
        
        while curr and curr.next:
            nn=curr.next
            
            curr.next = nn.next
            nn.next = curr
            
            if prev:
                prev.next = nn
                
            prev = curr
            curr = curr.next
            
        return head
        