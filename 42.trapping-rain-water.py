#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (62.90%)
# Likes:    32317
# Dislikes: 531
# Total Accepted:    2.3M
# Total Submissions: 3.6M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0] * len(height)
        m = 0
        for idx, h in enumerate(height):
            m = max(m, h)
            stack[idx] = m
        
        m = 0
        for idx, h in enumerate(reversed(height)):
            m = max(m, h)
            stack[len(height) - idx - 1] = min(m, stack[len(height) - idx - 1])
        
        total = 0
        for idx, h in enumerate(height):
            total += stack[idx] - h
        
        return total
# @lc code=end