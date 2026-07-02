"""
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

"""
class Solution:
    def makeUnion(self, head1, head2):
        # code here
        
        seen=set()
        
        dummy = Node(0)
        tail = dummy
        
        curr = head1
        while curr:
            if curr.data not in seen:
                seen.add(curr.data)
                tail.next = Node(curr.data)
                tail = tail.next
            curr = curr.next
        
        curr = head2
        while curr:
            if curr.data not in seen:
                seen.add(curr.data)
                tail.next = Node(curr.data)
                tail = tail.next
            curr = curr.next
        
        return dummy.next
        
        
        