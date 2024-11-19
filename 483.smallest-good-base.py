#
# @lc app=leetcode id=483 lang=python3
#
# [483] Smallest Good Base
#
# https://leetcode.com/problems/smallest-good-base/description/
#
# algorithms
# Hard (41.86%)
# Likes:    399
# Dislikes: 517
# Total Accepted:    24.1K
# Total Submissions: 57.6K
# Testcase Example:  '"13"'
#
# Given an integer n represented as a string, return the smallest good base of
# n.
#
# We call k >= 2 a good base of n, if all digits of n base k are 1's.
#
#
# Example 1:
#
#
# Input: n = "13"
# Output: "3"
# Explanation: 13 base 3 is 111.
#
#
# Example 2:
#
#
# Input: n = "4681"
# Output: "8"
# Explanation: 4681 base 8 is 11111.
#
#
# Example 3:
#
#
# Input: n = "1000000000000000000"
# Output: "999999999999999999"
# Explanation: 1000000000000000000 base 999999999999999999 is 11.
#
#
#
# Constraints:
#
#
# n is an integer in the range [3, 10^18].
# n does not contain any leading zeros.
#
#
#

# @lc code=start
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log(n, 2))
        for m in range(max_m, 1, -1):
            k = int(n ** (1/m))
            if k > 1:
                if (k ** (m + 1) - 1) // (k - 1) == n:
                    return str(k)
        return str(n - 1)
# @lc code=end

