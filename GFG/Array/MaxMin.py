import math
class Solution:
    def getMinMax(self, arr):
        MaxN=-math.inf
        MinN=math.inf
        for i in arr:
            if MaxN<=i:
                MaxN=i
            
            if MinN>=i:
                MinN=i
        return [MinN,MaxN]