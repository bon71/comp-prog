#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.86%)
# Likes:    4303
# Dislikes: 312
# Total Accepted:    677.2K
# Total Submissions: 1.5M
# Testcase Example:  '16'
#
# Given a positive integer num, return true if num is a perfect square or false
# otherwise.
#
# A perfect square is an integer that is the square of an integer. In other
# words, it is the product of some integer with itself.
#
# You must not use any built-in library function, such as sqrt.
#
#
# Example 1:
#
#
# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
#
#
# Example 2:
#
#
# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an
# integer.
#
#
#
# Constraints:
#
#
# 1 <= num <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        temp = 0
        while temp * temp <= num:
            if temp * temp == num:
                return True
            temp += 1
        return False
# @lc code=end

