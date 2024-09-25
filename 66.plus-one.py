#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (46.05%)
# Likes:    9568
# Dislikes: 5418
# Total Accepted:    2.5M
# Total Submissions: 5.4M
# Testcase Example:  '[1,2,3]'
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
# 
# Increment the large integer by one and return the resulting array of
# digits.
# 
# 
# Example 1:
# 
# 
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# 
# 
# Example 2:
# 
# 
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# 
# 
# Example 3:
# 
# 
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        up = 0
        length = len(digits)
        if length == 1:
            if digits == [9]:
                return [1,0]
        for i in range(length):
            if digits[length - 1 - i] == 9:
                up = 1
                digits[length - 1 - i] = (digits[length - 1 - i] + 1 ) % 10
                if length == i + 1:
                    return [1] + digits
            if up == 0:
                digits[length - 1 - i] += 1
                break
            up = 0
        return digits

# @lc code=end

