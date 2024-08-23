#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in list(set(ransomNote)):
            if ransomNote.count(letter) > magazine.count(letter): return False
        return True
# @lc code=end