"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""
class Solution(object):

    def longestCommonPrefix(self, strs):

        if not strs:
            return ''
        temp = min(strs)
        for i in range(len(temp)):
            for s in strs:
                if s[i] != temp[i]:
                    return temp[:i] if i > 0 else ''
        return temp
