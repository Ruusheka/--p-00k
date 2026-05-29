class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        cnt=0
        n=len(nums)
        for i in range(n):
            if count==0:
                count=1
                el=nums[i]
            elif nums[i]==el:
                count+=1
            else:
                count-=1
                
        for i in range(n):
            if nums[i]==el:
                cnt+=1

        if cnt>(n//2):
            return el


        