#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (34.36%)
# Likes:    29633
# Dislikes: 1810
# Total Accepted:    3.3M
# Total Submissions: 9.6M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        length, letters = 1, s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > length and s[i:j+1] == s[i:j+1][::-1]:
                    length = j-i+1
                    letters = s[i:j+1]

        return letters
# @lc code=end
