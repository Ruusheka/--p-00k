''' structure of linked list Node
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def addOne(self,head):
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
            
        
        head=rev(head)
        curr=head
        carry=1
        
        while curr and carry:               #999 (9+1)=10
            total=curr.data+carry           #+  1 10%10=0(curr.data)
            curr.data=total%10              #--------------- 10//10=1(carry)
            carry=total//10                 #0001
            
            if curr.next is None and carry:
                curr.next = Node(carry)
                carry=0
            
            curr=curr.next
            
        return rev(head)