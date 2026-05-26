#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        sumT=0
        num=str(n)
        for i in num:
            sumT+= pow(int(i),3)
        if sumT==n:
            return True
        else:
            return False