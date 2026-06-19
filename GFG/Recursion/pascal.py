class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here
	    res=[1]
	    prev=1
	    
	    for i in range(1,n):
	        curr=prev*(n-i)//i
	        res.append(curr)
	        prev=curr
	   
	    return res