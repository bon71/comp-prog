#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (47.19%)
# Likes:    10182
# Dislikes: 230
# Total Accepted:    717.8K
# Total Submissions: 1.5M
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: matrix = [["0"]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0
        mx = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1' : 
                    if i != 0 and j != 0:
                        matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i][j-1]), int(matrix[i-1][j])) + 1

                    mx = max(mx, int(matrix[i][j]))
        return int(mx)**2
# @lc code=end