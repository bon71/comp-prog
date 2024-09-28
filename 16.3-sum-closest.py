#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.03%)
# Likes:    10565
# Dislikes: 574
# Total Accepted:    1.3M
# Total Submissions: 2.8M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if sum(nums[-3::]) < target:
            return sum(nums[-3::])
        else:
            diff = float('inf')
            res = 0
            for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                head, tail = i + 1, len(nums)-1
                while head < tail:
                    sums = nums[i] + nums[head] + nums[tail]
                    if target == sums:
                        return sums
                    if diff > abs(target - sums):
                        res = sums
                        diff = abs(target - sums)
                    if sums < target:
                        head +=1
                    else:
                        tail -=1
            return res
# @lc code=end

