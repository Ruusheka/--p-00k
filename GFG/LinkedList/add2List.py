'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def addTwoLists(self, head1, head2):
        # code here
        def rev(head):
            prev=None
            curr=head
            
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            
            return prev
            
        
        head1=rev(head1)
        head2=rev(head2)
        
        carry=0
        dumm=Node(0)
        tail=dumm
        
        while head1 or head2 or carry:
            total=carry
            
            if head1:
                total+=head1.data
                head1=head1.next
            
            if head2:
                total+=head2.data
                head2=head2.next
                
            carry = total//10
            
            tail.next = Node(total%10)
            tail=tail.next
            
        
        ans=rev(dumm.next)
        
        while ans and ans.data ==0 and ans.next:
            ans=ans.next
            
        return ans