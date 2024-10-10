#
# @lc app=leetcode id=3306 lang=python3
#
# [3306] Count of Substrings Containing Every Vowel and K Consonants II
#
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/
#
# algorithms
# Medium (13.15%)
# Likes:    147
# Dislikes: 6
# Total Accepted:    9.3K
# Total Submissions: 46.3K
# Testcase Example:  '"aeioqq"\n1'
#
# You are given a string word and a non-negative integer k.
# 
# Return the total number of substrings of word that contain every vowel ('a',
# 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
# 
# 
# Example 1:
# 
# 
# Input: word = "aeioqq", k = 1
# 
# Output: 0
# 
# Explanation:
# 
# There is no substring with every vowel.
# 
# 
# Example 2:
# 
# 
# Input: word = "aeiou", k = 0
# 
# Output: 1
# 
# Explanation:
# 
# The only substring with every vowel and zero consonants is word[0..4], which
# is "aeiou".
# 
# 
# Example 3:
# 
# 
# Input: word = "ieaouqqieaouqq", k = 1
# 
# Output: 3
# 
# Explanation:
# 
# The substrings with every vowel and one consonant are:
# 
# 
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
# 
# 
# 
# 
# Constraints:
# 
# 
# 5 <= word.length <= 2 * 10^5
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
# 
# 
#

# @lc code=start
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        if k == 0:
            vowls = [word.count('a'),
                word.count('i'),
                word.count('u'),
                word.count('e'),
                word.count('o')
                ]
            if min(vowls) == 0:
                return 0
            else:
                return 1
        else:
            t_vowls = [word.count('a'),
                word.count('i'),
                word.count('u'),
                word.count('e'),
                word.count('o')
            ]
            print(t_vowls)



            res = 0
            vowls = ['a','i','u','e','o']
            temp = [0]*6
            for i in range(len(word)):
                if word[i] in vowls:
                    temp[vowls.index(word[i])] += 1
                else:
                    temp[-1] += 1

                if min(temp[0:4]) >= 1 and temp[-1] >= k:
                    print(temp)
                    res += 1
                    temp = [0]*6
            return res
# @lc code=end

