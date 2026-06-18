class Solution:
    def pattern(self, n):
        # code here
        res=[]
        
        def solve(n):
            res.append(n)
            
            if n<=0:
                return 0
            
            solve(n-5)
            res.append(n)
        
        solve(n)
        
        return res
            
            
        