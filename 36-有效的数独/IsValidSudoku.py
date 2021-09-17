# -*- coding: utf-8 -*-
# LeetCode 36-有效的数独

"""
Created on Fri Sept 17 18:30 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [[0] * 9 for _ in range(9)]
        for i in range(9):
            row = [0] * 9
            if i % 3 == 0:
                box = [[0] * 9 for _ in range(3)]
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = ord(board[i][j]) - ord('1')
                if row[num] or box[j // 3][num] or col[j][num]:
                    return False
                row[num] = 1
                box[j // 3][num] = 1
                col[j][num] = 1
        return True

        # hashes = [0] * 3
        # cols = [0] * 9
        # for k, line in enumerate(board):
        #     row = 0
        #     for i in range(9):
        #         if line[i] != '.':
        #             row += 10 ** int(line[i])
        #             hashes[i // 3] += 10 ** int(line[i])
        #             cols[i] += 10 ** int(line[i])
        #         else:
        #             continue
        #     r = str(row)
        #     if r.count('0') + r.count('1') != len(r):
        #         return False
        #     if k % 3 == 2:
        #         for i in range(3):
        #             h = str(hashes[i])
        #             if h.count('0') + h.count('1') != len(h):
        #                 return False
        #             hashes[i] = 0
        # for i in range(9):
        #     c = str(cols[i])
        #     if c.count('0') + c.count('1') != len(c):
        #         return False
        # return True


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
