#
# @lc app=leetcode id=3352 lang=python3
#
# [3352] Count K-Reducible Numbers Less Than N
#
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/description/
#
# algorithms
# Hard (20.65%)
# Likes:    43
# Dislikes: 2
# Total Accepted:    2.5K
# Total Submissions: 9.4K
# Testcase Example:  '"111"\n1'
#
# You are given a binary string s representing a number n in its binary form.
#
# You are also given an integer k.
#
# An integer x is called k-reducible if performing the following operation at
# most k times reduces it to 1:
#
#
# Replace x with the count of set bits in its binary representation.
#
#
# For example, the binary representation of 6 is "110". Applying the operation
# once reduces it to 2 (since "110" has two set bits). Applying the operation
# again to 2 (binary "10") reduces it to 1 (since "10" has one set bit).
#
# Return an integer denoting the number of positive integers less than n that
# are k-reducible.
#
# Since the answer may be too large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: s = "111", k = 1
#
# Output: 3
#
# Explanation:
#
# n = 7. The 1-reducible integers less than 7 are 1, 2, and 4.
#
#
# Example 2:
#
#
# Input: s = "1000", k = 2
#
# Output: 6
#
# Explanation:
#
# n = 8. The 2-reducible integers less than 8 are 1, 2, 3, 4, 5, and 6.
#
#
# Example 3:
#
#
# Input: s = "1", k = 3
#
# Output: 0
#
# Explanation:
#
# There are no positive integers less than n = 1, so the answer is 0.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 800
# s has no leading zeros.
# s consists only of the characters '0' and '1'.
# 1 <= k <= 5
#
#
#

# @lc code=start
class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = int(s, 2)
        dp = [[0] * 2 for _ in range(800)]
        dp[0][0] = 1
        for i in range(1, 800):
            dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
            dp[i][1] = dp[i-1][0]
        def count(x):
            if x == 0:
                return 0
            ans = 0
            for i in range(800):
                if dp[i][1] > x:
                    break
                ans += dp[i][0]
                if dp[i][1] == x:
                    break
            return ans
        return count(n) - count(n + 1)
# @lc code=end

