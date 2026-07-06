'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        zeroH=Node(-1)
        oneH=Node(-1)
        twoH=Node(-1)
        
        zero=zeroH
        one=oneH
        two=twoH
        
        curr=head
        
        while curr:
            if curr.data==0:
                zero.next=curr
                zero=zero.next
            elif curr.data==1:
                one.next=curr
                one=one.next
            else:
                two.next=curr
                two=two.next
            
            curr=curr.next
            
        if oneH.next:
            zero.next=oneH.next
        else:
            zero.next=twoH.next
        
        one.next=twoH.next
        
        two.next=None
            
        return zeroH.next
            
            