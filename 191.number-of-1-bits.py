#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
# https://leetcode.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (72.29%)
# Likes:    6560
# Dislikes: 1341
# Total Accepted:    1.6M
# Total Submissions: 2.2M
# Testcase Example:  '11'
#
# Write a function that takes the binary representation of a positive integer
# and returns the number of set bits it has (also known as the Hamming
# weight).
# 
# 
# Example 1:
# 
# 
# Input: n = 11
# 
# Output: 3
# 
# Explanation:
# 
# The input binary string 1011 has a total of three set bits.
# 
# 
# Example 2:
# 
# 
# Input: n = 128
# 
# Output: 1
# 
# Explanation:
# 
# The input binary string 10000000 has a total of one set bit.
# 
# 
# Example 3:
# 
# 
# Input: n = 2147483645
# 
# Output: 30
# 
# Explanation:
# 
# The input binary string 1111111111111111111111111111101 has a total of thirty
# set bits.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
# 
# Follow up: If this function is called many times, how would you optimize it?
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n%2
            n = n//2
        return res
# @lc code=end

