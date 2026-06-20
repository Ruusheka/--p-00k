class Solution:
    def binarySearch(self, arr, k):
        # code here
        for i in arr:
            if i==k:
                return True
        
        return False
        