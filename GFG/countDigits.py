#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count=0
        num=str(n)
        for i in num:
            if i != '0' and n % int(i) == 0:
                count += 1
        return count