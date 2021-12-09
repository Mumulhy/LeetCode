# -*- coding: utf-8 -*-
# LeetCode 794-有效的井字游戏

"""
Created on Thu Dec 9 22:24 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        X, O = 0, 0
        lines = [0] * 8
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    score = 1
                    X += 1
                elif board[i][j] == 'O':
                    score = -1
                    O += 1
                else:
                    continue
                lines[i] += score
                lines[j + 3] += score
                if i == j:
                    lines[6] += score
                if i + j == 2:
                    lines[7] += score
        if O > X or X > O + 1:
            return False
        X_win, O_win = lines.count(3), lines.count(-3)
        if (X == O and X_win) or (X > O and O_win):
            return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validTicTacToe(["OXX", "XOX", "OXO"]))
