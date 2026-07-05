class Solution(object):
    def majorityElement(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        candi=None
        for i in arr:
            if cnt==0:
                candi=i
                cnt+=1
            elif i==candi:
                cnt+=1
            else:
                cnt-=1
        
        c=0
        for i in arr:
            if i==candi:
                c+=1
        
        if c>len(arr)//2:
            return candi
        
        return -1
