# -*- coding: utf-8 -*-
# LeetCode 417-太平洋大西洋水流问题

"""
Created on Wed Apr 27 10:46 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        oceans = [[[False] * n for _ in range(m)] for _ in range(2)]

        diff = [-1, 0, 1, 0, -1]
        for ocean in range(2):
            if ocean == 0:
                stack = {(0, j) for j in range(n)} | {(i, 0) for i in range(m)}
            else:
                stack = {(m - 1, j) for j in range(n)} | {(i, n - 1) for i in range(m)}
            while stack:
                for x, y in stack:
                    oceans[ocean][x][y] = True
                new_stack = set()
                for x, y in stack:
                    for k in range(4):
                        neighbour_x, neighbour_y = x + diff[k], y + diff[k + 1]
                        if (0 <= neighbour_x < m and 0 <= neighbour_y < n
                                and heights[neighbour_x][neighbour_y] >= heights[x][y]
                                and not oceans[ocean][neighbour_x][neighbour_y]):
                            new_stack.add((neighbour_x, neighbour_y))
                stack = new_stack

        ans = []
        for i in range(m):
            for j in range(n):
                if oceans[0][i][j] is oceans[1][i][j] is True:
                    ans.append([i, j])
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.pacificAtlantic([[2, 1], [1, 2]]))
