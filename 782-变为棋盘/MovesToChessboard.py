# -*- coding: utf-8 -*-
# LeetCode 782-变为棋盘

"""
Created on Tues Aug 23 09:56 2022

@author: _Mumu
Environment: py39
"""

from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        line = board[0]
        col = [raw[0] for raw in board]
        cnt1 = Counter(line)
        if abs(cnt1[0] - cnt1[1]) > 1:
            return -1
        cnt2 = Counter(col)
        if abs(cnt2[0] - cnt2[1]) > 1:
            return -1
        for another in board[1:]:
            if not (all(digit == another_digit for digit, another_digit in zip(line, another)) or
                    all(digit != another_digit for digit, another_digit in zip(line, another))):
                return -1

        def moves(arr: List[int], counter: Counter) -> int:
            a, b = 0, 1
            if counter[a] < counter[b]:
                a, b = 1, 0
            is_odd = (counter[a] + counter[b]) & 1
            move = sum(num == b for num in arr[::2])
            return move if is_odd else min(move, (counter[a] + counter[b]) // 2 - move)

        return moves(line, cnt1) + moves(col, cnt2)


if __name__ == '__main__':
    s = Solution()
    print(s.movesToChessboard(board=[[1, 0], [1, 0]]))
