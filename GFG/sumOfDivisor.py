class Solution:
    def sumOfDivisors(self, n):
        sumT = 0
        for i in range(1, n + 1):
            sumT+=i*(n//i)
        return sumT