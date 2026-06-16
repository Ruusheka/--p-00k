class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        n=len(mat)
        m=len(mat[0])
        
        k=k%m
        
        res=[]
        
        for row in mat:
            new_row = row[k:]+row[:k]
            res.append(new_row)
            
        return res