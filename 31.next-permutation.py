#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (40.97%)
# Likes:    18715
# Dislikes: 4764
# Total Accepted:    1.5M
# Total Submissions: 3.7M
# Testcase Example:  '[1,2,3]'
#
# A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.
#
#
# For example, for arr = [1,2,3], the following are all the permutations of
# arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
#
#
# The next permutation of an array of integers is the next lexicographically
# greater permutation of its integer. More formally, if all the permutations of
# the array are sorted in one container according to their lexicographical
# order, then the next permutation of that array is the permutation that
# follows it in the sorted container. If such arrangement is not possible, the
# array must be rearranged as the lowest possible order (i.e., sorted in
# ascending order).
#
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does
# not have a lexicographical larger rearrangement.
#
#
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: [1,3,2]
#
#
# Example 2:
#
#
# Input: nums = [3,2,1]
# Output: [1,2,3]
#
#
# Example 3:
#
#
# Input: nums = [1,1,5]
# Output: [1,5,1]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Find the first decreasing element from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Find the first element greater than the decreasing element
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap the two elements
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the array from i + 1 to the end
        nums[i + 1:] = reversed(nums[i + 1:])

        return nums
# @lc code=end

