#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.17%)
# Likes:    12072
# Dislikes: 455
# Total Accepted:    1.5M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# 
# Output: [2,1,4,3]
# 
# Explanation:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = []
# 
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: head = [1]
# 
# Output: [1]
# 
# 
# Example 4:
# 
# 
# Input: head = [1,2,3]
# 
# Output: [2,1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            if current.next.next:
                current = current.next.next
            else:
                break
        return head
# @lc code=end

