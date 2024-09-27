#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
#
# algorithms
# Easy (81.50%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    46.9K
# Total Submissions: 57.4K
# Testcase Example:  '[2,1,3,5,6]\n5\n2'
#
# You are given an integer array nums, an integer k, and an integer
# multiplier.
# 
# You need to perform k operations on nums. In each operation:
# 
# 
# Find the minimum value x in nums. If there are multiple occurrences of the
# minimum value, select the one that appears first.
# Replace the selected minimum value x with x * multiplier.
# 
# 
# Return an integer array denoting the final state of nums after performing all
# k operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,1,3,5,6], k = 5, multiplier = 2
# 
# Output: [8,4,6,5,6]
# 
# Explanation:
# 
# 
# 
# 
# Operation
# Result
# 
# 
# After operation 1
# [2, 2, 3, 5, 6]
# 
# 
# After operation 2
# [4, 2, 3, 5, 6]
# 
# 
# After operation 3
# [4, 4, 3, 5, 6]
# 
# 
# After operation 4
# [4, 4, 6, 5, 6]
# 
# 
# After operation 5
# [8, 4, 6, 5, 6]
# 
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2], k = 3, multiplier = 4
# 
# Output: [16,8]
# 
# Explanation:
# 
# 
# 
# 
# Operation
# Result
# 
# 
# After operation 1
# [4, 2]
# 
# 
# After operation 2
# [4, 8]
# 
# 
# After operation 3
# [16, 8]
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 10
# 1 <= multiplier <= 5
# 
# 
#

# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minimum = min(nums)
            target_index = nums.index(minimum)
            nums[target_index] *= multiplier
        return nums
# @lc code=end

