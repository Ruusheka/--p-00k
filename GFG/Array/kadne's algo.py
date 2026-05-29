import math
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        sumT=0
        maxIn=-math.inf
        
        for i in range(len(arr)):
            sumT+=arr[i]
            if (sumT > maxIn):
                maxIn=sumT
            if sumT< 0:
                sumT=0
                
        return maxIn