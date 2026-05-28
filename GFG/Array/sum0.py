class Solution:
    def findTriplets(self, arr):
        arr.sort()
        n=len(arr)
        
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                sumT=arr[left]+arr[right]+arr[i]
                if sumT==0:
                    return True
                elif sumT>0:
                    right-=1
                elif sumT<0:
                    left+=1
        
        return False
                