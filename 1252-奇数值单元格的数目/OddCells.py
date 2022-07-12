# -*- coding: utf-8 -*-
# LeetCode 1252-奇数值单元格的数目

"""
Created on Tues Jul 12 10:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        oddr = sum(rows)
        oddc = sum(cols)
        return oddr * (n - oddc) + oddc * (m - oddr)

        # grid = [[0] * n for _ in range(m)]
        # for r, c in indices:
        #     for j in range(n):
        #         grid[r][j] ^= 1
        #     for i in range(m):
        #         grid[i][c] ^= 1
        # return sum(sum(row) for row in grid)


if __name__ == '__main__':
    s = Solution()
    print(s.oddCells(m=2, n=2, indices=[[1, 1], [0, 0]]))
