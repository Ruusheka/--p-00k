class Solution:
    def isPerfect(self, n):
        sumT=1
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                sumT+=i
                if i!=n//i:
                    sumT+=n//i
        
        return sumT==n