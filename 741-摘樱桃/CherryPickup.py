# -*- coding: utf-8 -*-
# LeetCode 741-摘樱桃

"""
Created on Sun Jul 10 11:03 2022

@author: _Mumu
Environment: py38
"""

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[float('-inf')] * n for _ in range(n)]
        f[0][0] = grid[0][0]
        for k in range(1, n * 2 - 1):
            for x1 in range(min(k, n - 1), max(k - n, -1), -1):
                for x2 in range(min(k, n - 1), x1 - 1, -1):
                    y1, y2 = k - x1, k - x2
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        f[x1][x2] = float('-inf')
                        continue
                    res = f[x1][x2]
                    if x1:
                        res = max(res, f[x1 - 1][x2])
                    if x2:
                        res = max(res, f[x1][x2 - 1])
                    if x1 and x2:
                        res = max(res, f[x1 - 1][x2 - 2])
                    res += grid[x1][y1]
                    if x2 != x1:
                        res += grid[x2][y2]
                    f[x1][x2] = res
        return max(f[-1][-1], 0)

if __name__ == '__main__':
    s = Solution()
    print(s.cherryPickup([[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]))