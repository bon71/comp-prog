#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (51.41%)
# Likes:    15208
# Dislikes: 1355
# Total Accepted:    1.6M
# Total Submissions: 3.2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])

        if m == 1:
            return matrix.pop(0)

        if n == 1:
            for i in range(m):
                res.append(matrix[i].pop(0))
            return res

        res += matrix.pop(0)
        dump = []
        for i in range(m-1):
            res.append(matrix[i].pop(-1))
            dump.append(matrix[i].pop(0))
        res += matrix.pop(-1)[::-1]
        res += dump[::-1]
        if len(matrix) == 0 or matrix[0] == []:
            return res
        else:
            return res + self.spiralOrder(matrix)
# @lc code=end

