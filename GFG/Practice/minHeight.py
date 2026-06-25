class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        n=len(arr)
        
        ans=arr[n-1]-arr[0]
        
        for i in range(n-1):
            if arr[i+1]-k<0:
                continue
            mini = min(arr[0]+k,arr[i+1]-k)   
            maxi = max(arr[i]+k,arr[n-1]-k)
            
            ans=min(ans,maxi-mini)
            
        return ans