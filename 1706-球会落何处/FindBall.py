# -*- coding: utf-8 -*-
# LeetCode 1706-球会落何处

"""
Created on Thu Feb 24 20:09 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(n):
            x = i
            for j in range(m):
                if (((x == 0 or grid[j][x - 1] == 1) and grid[j][x] == -1)
                        or ((x == n - 1 or grid[j][x + 1] == -1) and grid[j][x] == 1)):
                    x = -1
                    break
                x += grid[j][x]
            ans.append(x)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findBall([[1, 1, 1, 1, 1, 1],
                      [-1, -1, -1, -1, -1, -1],
                      [1, 1, 1, 1, 1, 1],
                      [-1, -1, -1, -1, -1, -1]]))
