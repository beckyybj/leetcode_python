"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution(object):

    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        if x > 10 and x % 10 == 0:
            return False

        res = []
        temp = x
        while temp > 0:
            res.append(temp % 10)
            temp = temp // 10

        for i, n in enumerate(res):
            temp += n * (10**(len(res) - i - 1))

        return temp == x
