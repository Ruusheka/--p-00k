class Solution:
    def minRow(self,a):
        #code here
        res=1
        min_count=math.inf
        
        for i in range(len(a)):
            total=sum(a[i])
            
            if total<min_count:
                min_count=total
                res=i+1
        
        return res
                
        