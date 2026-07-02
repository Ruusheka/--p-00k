""" Structure of linked list Node
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        
        prev=None
        curr=head
        cnt=0
        
        while curr and cnt<k:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            cnt+=1
        
        if curr:
            head.next = self.reverseKGroup(curr,k)
        
        return prev