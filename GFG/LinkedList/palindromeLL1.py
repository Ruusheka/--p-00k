'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        stack=[]

        curr=head
        while curr:
            stack.append(curr.data)
            curr=curr.next
        
        curr=head
        while curr:
            if curr.data!=stack.pop():
                return False
            curr=curr.next
        
        return True