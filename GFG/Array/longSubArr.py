class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        pre_sum = 0
        maxi = 0
        seen = {}
        
        for i in range(len(arr)):
            pre_sum+=arr[i]
            
            if pre_sum == k:
                maxi=i+1
            
            if pre_sum-k in seen:
                maxi = max(maxi,i-seen[pre_sum-k])
            
            
            if pre_sum not in seen:
                seen[pre_sum] = i
                
        return maxi
