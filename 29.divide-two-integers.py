#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (17.73%)
# Likes:    5286
# Dislikes: 14889
# Total Accepted:    813.1K
# Total Submissions: 4.6M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
# The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335
# would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
#
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
# problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31
# - 1, and if the quotient is strictly less than -2^31, then return -2^31.
#
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
#
#
# Constraints:
#
#
# -2^31 <= dividend, divisor <= 2^31 - 1
# divisor != 0
#
#
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)
        if res >= 2**31 - 1:
            return 2**31 - 1
        elif res <= -1 * 2 **31:
            return -1 * 2 **31
        else:
            return res

# @lc code=end

