#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (47.95%)
# Likes:    6878
# Dislikes: 438
# Total Accepted:    1.4M
# Total Submissions: 3M
# Testcase Example:  '1'
#
# Given an integer n, return true if it is a power of two. Otherwise, return
# false.
# 
# An integer n is a power of two, if there exists an integer x such that n ==
# 2^x.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: true
# Explanation: 2^0 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 16
# Output: true
# Explanation: 2^4 = 16
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# -2^31 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        return int(bin(n)[3::]) == 0
# @lc code=end

