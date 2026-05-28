class Solution:
    def removeDuplicates(self, arr):
        seen=set()
        res=[]
        for i in arr:
            if i not in seen:
                seen.add(i)
                res.append(i)
                
        return res