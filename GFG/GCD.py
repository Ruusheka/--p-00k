class Solution:
    def gcd(self, a, b):
        rem=1
        if a>b:
            divident=a
            divisor=b
        else:
            divident=b
            divisor=a
        while rem!=0:
            rem=divident%divisor
            if rem!=0:
                divident=divisor
                divisor=rem
        return divisor