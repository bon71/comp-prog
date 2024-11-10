#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (79.48%)
# Likes:    17625
# Dislikes: 287
# Total Accepted:    2.2M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of unique elements, return all possible subsets
# (the power set).
#
# The solution set must not contain duplicate subsets. Return the solution in
# any order.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# Example 2:
#
#
# Input: nums = [0]
# Output: [[],[0]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# All the numbers of nums are unique.
#
#
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path + [nums[i]])
        backtrack(0, [])
        return res
# @lc code=end

