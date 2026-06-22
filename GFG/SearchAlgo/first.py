class Solution:
    def find(self, arr, x):
        # code here
        ans=[]
        for i in range(len(arr)):
            if arr[i]==x:
                ans.append(i)
        
        if not ans:
            return [-1, -1]
        
        
            
        return ([ans[0],ans[-1]])