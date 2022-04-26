# -*- coding: utf-8 -*-
# LeetCode 883-三维形体投影面积

"""
Created on Tues Apr 26 09:33 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        col_max = [0] * n
        for i in range(m):
            raw_max = 0
            for j in range(n):
                if grid[i][j]:
                    ans += 1
                col_max[j] = max(col_max[j], grid[i][j])
                raw_max = max(raw_max, grid[i][j])
            ans += raw_max
        ans += sum(col_max)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[2, 0]]))
