#
# @lc app=leetcode id=3295 lang=python3
#
# [3295] Report Spam Message
#
# https://leetcode.com/problems/report-spam-message/description/
#
# algorithms
# Medium (47.08%)
# Likes:    76
# Dislikes: 10
# Total Accepted:    44.6K
# Total Submissions: 94.5K
# Testcase Example:  '["hello","world","leetcode"]\n["world","hello"]'
#
# You are given an array of strings message and an array of strings
# bannedWords.
# 
# An array of words is considered spam if there are at least two words in it
# that exactly match any word in bannedWords.
# 
# Return true if the array message is spam, and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: message = ["hello","world","leetcode"], bannedWords =
# ["world","hello"]
# 
# Output: true
# 
# Explanation:
# 
# The words "hello" and "world" from the message array both appear in the
# bannedWords array.
# 
# 
# Example 2:
# 
# 
# Input: message = ["hello","programming","fun"], bannedWords =
# ["world","programming","leetcode"]
# 
# Output: false
# 
# Explanation:
# 
# Only one word from the message array ("programming") appears in the
# bannedWords array.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= message.length, bannedWords.length <= 10^5
# 1 <= message[i].length, bannedWords[i].length <= 15
# message[i] and bannedWords[i] consist only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        taboo = set(bannedWords)
        for i in message:
            if i in taboo:
                count += 1
            if count >= 2:
                return True
        return False
# @lc code=end

