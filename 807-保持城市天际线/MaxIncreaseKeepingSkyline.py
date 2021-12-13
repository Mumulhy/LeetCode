# -*- coding: utf-8 -*-
# LeetCode 807-保持城市天际线

"""
Created on Mon Dec 13 13:37 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[i][j] for i in range(n)) for j in range(n)]
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += min(row_max[i], col_max[j])
        ans -= sum(sum(grid, start=[]))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]))
