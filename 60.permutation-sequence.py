#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Hard (48.35%)
# Likes:    6777
# Dislikes: 485
# Total Accepted:    433.2K
# Total Submissions: 895.8K
# Testcase Example:  '3\n3'
#
# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
#
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
#
#
# Given n and k, return the k^th permutation sequence.
#
#
# Example 1:
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
# Input: n = 4, k = 9
# Output: "2314"
# Example 3:
# Input: n = 3, k = 1
# Output: "123"
#
#
# Constraints:
#
#
# 1 <= n <= 9
# 1 <= k <= n!
#
#
#

# @lc code=start
import itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(i for i in range(1, n+1))
        res = list(itertools.permutations(nums))
        if k > len(res):
            return ""
        else:
            ans = ''
            for i in res[k-1]:
                ans = ans + str(i)
        return ans
# @lc code=end

