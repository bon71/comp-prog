#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (64.73%)
# Likes:    4880
# Dislikes: 346
# Total Accepted:    943.1K
# Total Submissions: 1.5M
# Testcase Example:  '3'
#
# Given an integer rowIndex, return the rowIndex^th (0-indexed) row of the
# Pascal's triangle.
# 
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it as shown:
# 
# 
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:
# Input: rowIndex = 0
# Output: [1]
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
# 
# 
# Constraints:
# 
# 
# 0 <= rowIndex <= 33
# 
# 
# 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra
# space?
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - k + 1) // k
            res.append(next_val)
            prev = next_val
        return res
# @lc code=end

