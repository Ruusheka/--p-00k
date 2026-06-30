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
        
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        
        temp=head
        for _ in range((count-1)//2):
            temp=temp.next
        
        nn.next=temp.next
        temp.next=nn
        
        return head

