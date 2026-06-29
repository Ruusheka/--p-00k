'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        if fast:
            slow=slow.next
        
        prev=None
        curr=slow
        
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        first=head
        second=prev
        
        while second:
            if first.data!=second.data:
                return False
            
            first=first.next
            second=second.next
        
        return True
        
        