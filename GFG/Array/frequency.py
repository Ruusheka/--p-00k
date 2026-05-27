class Solution:
    def frequencyCount(self, arr):
        #  code here
        n=len(arr)
        new=[0]*n
        
        for i in arr:
            new[i-1]+=1
        
        return new