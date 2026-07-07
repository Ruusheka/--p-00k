# Structure of a link list node
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        # code here
        if head is None or head.next is None:
            return head
            
        evenH=evenT=None
        oddH=oddT=None
        
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = None
            
            if curr.data % 2 ==0:
                if evenH is None:
                    evenH = evenT = curr
                else:
                    evenT.next = curr
                    evenT=curr
            else:
                if oddH is None:
                    oddH = oddT = curr
                else:
                    oddT.next = curr
                    oddT = curr
                    
                    
            curr=nxt
            
        if evenH is None:
            return oddH
            
        evenT.next = oddH
        return evenH