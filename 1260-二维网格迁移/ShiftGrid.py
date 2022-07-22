# -*- coding: utf-8 -*-
# LeetCode 1260-二维网格迁移

"""
Created on Wed Jul 20 10:14 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m * n
        if k % n == 0:
            c = k // n
            return grid[-c:] + grid[:-c]
        l = sum(grid, start=[])
        l = l[-k:] + l[:-k]
        return list(l[i * n:(i + 1) * n] for i in range(m))


if __name__ == '__main__':
    s = Solution()
    print(s.shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9))
