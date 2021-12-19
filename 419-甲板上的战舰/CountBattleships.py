# -*- coding: utf-8 -*-
# LeetCode 419-甲板上的战舰

"""
Created on Sat Dec 18 23:35 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == 'X' and not ((i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')):
                    ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.countBattleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
