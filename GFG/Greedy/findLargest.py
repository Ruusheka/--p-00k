class Solution:
    def findLargest(self, n, s):
        if s>9*n:
            return '-1'
        
        if s==0:
            if n==1:
                return '0'
            else:
                return '-1'
                
        ans=[]
        
        for _ in range(n):
            digit=min(9,s)
            ans.append(str(digit))
            s-=digit
        
        return ''.join(ans)