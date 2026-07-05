def merge(self,interval):
    interval.sort()
    
    merged=[]
    
    for i in interval:
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])
        
    return merged

#class Solution(object):
    # def merge(self, intervals):
    #     """
    #     :type intervals: List[List[int]]
    #     :rtype: List[List[int]]
    #     """
    #     intervals.sort()

    #     ans=[]

    #     for i in intervals:
    #         st,en=i # [2,6] start=2,end=6

    #         #in list ans checks with last appended element that suppose [1,3] =>  3<6 so it goes to else part and updates the list else, it just append the list 
    #         if not ans or st>ans[-1][1]: 
    #             ans.append([st,en])
    #         else:
    #             ans[-1][1] = max(ans[-1][1],en)
            
    #     return ans
