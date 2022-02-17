# -*- coding: utf-8 -*-
# LeetCode 688-骑士在棋盘上的概率

"""
Created on Thu Feb 17 16:22 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if 2 * k <= row < n - 2 * k and 2 * k <= column < n - 2 * k:
            return 1
        if n < 3 or row < 0 or row >= n or column < 0 or column >= n:
            return 0

        diff = [-2, -1, -2, 1, 2, -1, 2, 1, -2]
        next_pos = []
        for x in range(n):
            line = []
            for y in range(n):
                tmp = []
                for i in range(8):
                    nx, ny = x + diff[i], y + diff[i + 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        tmp.append((nx, ny))
                line.append(tmp)
            next_pos.append(line)

        board = [[0] * n for _ in range(n)]
        board[row][column] = 1
        loop = k
        while loop:
            loop -= 1
            new_board = [[0] * n for _ in range(n)]
            for x in range(n):
                for y in range(n):
                    if board[x][y] > 0:
                        for nx, ny in next_pos[x][y]:
                            new_board[nx][ny] += board[x][y]
            board = new_board

        return sum(sum(board, start=[])) * 0.125 ** k

        # if k == 0 and 0 <= row < n and 0 <= column < n:
        #     return 1
        # dp = [[[0] * n for _ in range(n)] for _ in range(k)]
        # for x in range(n):
        #     for y in range(n):
        #         dp[0][x][y] = 1
        # diff = [-2, -1, -2, 1, 2, -1, 2, 1, -2]
        # for step in range(k - 1):
        #     for x in range(n):
        #         for y in range(n):
        #             dp[step + 1][x][y] = sum(dp[step][x + diff[i]][y + diff[i + 1]]
        #                                      for i in range(8)
        #                                      if 0 <= x + diff[i] < n and 0 <= y + diff[i + 1] < n) / 8
        # return sum(dp[k - 1][row + diff[i]][column + diff[i + 1]]
        #            for i in range(8)
        #            if 0 <= row + diff[i] < n and 0 <= column + diff[i + 1] < n) / 8


if __name__ == '__main__':
    s = Solution()
    print(s.knightProbability(n=3, k=2, row=0, column=0))
