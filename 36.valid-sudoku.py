#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box = [
            # left top
            [board[0][0:3] + board[1][0:3] + board[2][0:3]],
            # center top
            [board[0][3:6] + board[1][3:6] + board[2][3:6]],
            # right top
            [board[0][6:9] + board[1][6:9] + board[2][6:9]],
            # left middle
            [board[3][0:3] + board[4][0:3] + board[5][0:3]],
            # center middle
            [board[3][3:6] + board[4][3:6] + board[5][3:6]],
            # right middle
            [board[3][6:9] + board[4][6:9] + board[5][6:9]],
            # left bottom
            [board[6][0:3] + board[7][0:3] + board[8][0:3]],
            # center bottom
            [board[6][3:6] + board[7][3:6] + board[8][3:6]],
            # right bottom
            [board[6][6:9] + board[7][6:9] + board[8][6:9]],
        ]
        reverse = [[]*9]*9
        
        for i in range(10):
            for j in range(10):
                reverse[j][i] = list[i][j]

        for k in range(10):
            for y in range(10):
                if board[k].count(y) > 1 or box[k].count(y) > 1 or reverse[k].count(y) > 1:
                    return False
        
        return True

# @lc code=end

