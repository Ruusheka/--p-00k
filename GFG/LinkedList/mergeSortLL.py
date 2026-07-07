''' Structure of a Linked List node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        # code here
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        left = self.mergeSort(head)
        right = self.mergeSort(mid)
        
        return self.merge(left,right)
        
    
    def merge(self,head1,head2):
        dummy = Node(-1)
        tail = dummy
        
        while head1 and head2:
            if head1.data <= head2.data:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            
            tail = tail.next
            
        #if any one one the line is over, simpley appending, the entire second lline to the existing line  i.e tail
        if head1:
            tail.next = head1
        else:
            tail.next = head2
            
        return dummy.next
        
        
        