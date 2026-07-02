'''Structure of a link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def countPairs(self, head1, head2, x):
        # code here
        s=set()
        curr=head2
        count=0
        
        while curr:
            s.add(curr.data)
            curr=curr.next
            
        curr=head1
        while curr:
            if x-curr.data in s:
                count+=1
            curr = curr.next
        
        
        return count
                