class Solution:
    def maxWater(self, arr):
        # code here
        left=0
        right=len(arr)-1
        water=0
        l_max=0
        r_max=0
        
        while left<=right:
            
            if arr[left] <= arr[right]:
                
                if arr[left]>=l_max:
                    l_max = arr[left]
                else:
                    water+=l_max - arr[left]
                left+=1
            else:
                if arr[right]>=r_max:
                    r_max = arr[right]
                else:
                    water+=r_max - arr[right]
                right-=1
        
        return water
                