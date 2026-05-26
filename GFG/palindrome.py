class Solution:
    def isPalindrome(self, n):
        num=str(abs(n))
        if num[ : : -1] ==num:
            return True
        else:
            return False