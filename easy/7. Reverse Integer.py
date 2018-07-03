# Given a 32-bit signed integer, reverse digits of an integer.
# Example :
#
# Input: 123
# Output: 321

# Input: -123
# Output: -321

# Input: 120
# Output: 21

class Solution(object):
    def reverse(self, x):
        sign=1
        if x<0:
            sign=-1
        t=sign*(int(str(abs(x))[::-1]))
        if((t>=(2**31-1)) or (t<=(-2**31))):
            t=0
        return t