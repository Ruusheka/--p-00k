class Solution:
    def matrixDiagonally(self, mat):
        # code here
        n=len(mat)
        res=[]
        
        for i in range(2*n-1):
            temp=[]
            
            if i<n:
                r=0
            else:
                r=i-n+1
            
            if i<n:
                c=i
            else:
                c=n-1
            
            
            while r<n and c>=0:
                temp.append(mat[r][c])
                r+=1
                c-=1
            
            if i%2==0:
                temp.reverse()
                
            res.extend(temp)
            
        return res
            