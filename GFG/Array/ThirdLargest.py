import math
class Solution:
    def thirdLargest(self,arr):
        if len(arr)<=2:
            return -1
        
        first=second=third=-math.inf 
        
        for num in arr:
            if num>=first:
                third=second
                second=first
                first=num
            elif num>=second:
                third=second
                second=num
            elif num>=third:
                third=num
        
        return third