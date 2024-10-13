#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.01%)
# Likes:    7155
# Dislikes: 3405
# Total Accepted:    863.6K
# Total Submissions: 2.1M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
# 
# 
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# 
# 
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
       return str(int(num1)*int(num2))
# @lc code=end

