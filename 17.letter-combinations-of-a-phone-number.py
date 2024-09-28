#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (61.58%)
# Likes:    18875
# Dislikes: 1018
# Total Accepted:    2.2M
# Total Submissions: 3.6M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = ""
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.patterns ={
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        return

    def combineTwoArrays(self, original: list[str], add: list[str]) -> list[str]:
        ans = []
        for i in range(len(original)):
            for j in range(len(add)):
                word = original[i] + add[j]
                ans.append(word)
        return ans

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.patterns[digits]
        else:
            res = []
            for i in range(len(digits)-1):
                if res == []:
                    res = self.patterns[digits[i]]
                res = self.combineTwoArrays(res,self.patterns[digits[i+1]])
            return res
# @lc code=end

