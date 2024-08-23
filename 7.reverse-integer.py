#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        pm = 1
        if x < 0:
            pm = -1
            x *= pm
        result = int(str(x)[::-1]) * pm
        if result > 2**31 or result < -2**31:
            return 0
        else:
            return result
# @lc code=end

