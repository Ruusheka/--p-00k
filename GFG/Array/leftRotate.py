class Solution:
    def rotateArr(self, arr, d):
        k=d%len(arr)
        
        l,r=0,k-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l,r=l+1,r-1
        
        l,r=k,len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l,r=l+1,r-1
            
        l,r=0,len(arr)-1
        while l<r:
            arr[l],arr[r]=arr[r],arr[l]
            l,r=l+1,r-1
        
        