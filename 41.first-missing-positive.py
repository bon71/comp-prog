#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (40.09%)
# Likes:    17094
# Dislikes: 1876
# Total Accepted:    1.3M
# Total Submissions: 3.3M
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums.
#
# You must implement an algorithm that runs in O(n) time and uses O(1)
# auxiliary space.
#
#
# Example 1:
#
#
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.
#
#
# Example 2:
#
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.
#
#
# Example 3:
#
#
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        nums = set(nums)
        while res in nums:
            res += 1
        return res

# @lc code=end

