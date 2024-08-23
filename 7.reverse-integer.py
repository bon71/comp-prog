#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        pm = 1
        if x == 0:
            return x
        if x < 0:
            pm = -1
            x *= pm
        list_x = list(str(x))
        list_x.reverse()
        str_result = ''
        for str_x in list_x:
            str_result = str_result + str_x
        result = int(str_result) * pm
        if result > 2**31 or result < -2**31:
            return 0
        else:
            return result
# @lc code=end

