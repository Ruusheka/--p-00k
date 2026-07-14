# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        curr = head
        
        while curr:
            for i in range(1,m):
                if curr is None:
                    return
                curr = curr.next
                
            
            if curr is None:
                return
            
            temp = curr.next
            for i in range(n):
                if temp is None:
                    break
                temp = temp.next
                
            curr.next = temp
            curr=temp