# -*- coding: utf-8 -*-
# LeetCode 1219-黄金矿工

"""
Created on Sun Feb 6 12:04 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        diff = [-1, 0, 1, 0, -1]
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(x: int, y: int, curr_sum: int) -> None:
            nonlocal ans
            curr_gold = grid[x][y]
            curr_sum += curr_gold
            grid[x][y] = 0

            neighbours = []
            for i in range(4):
                neighbour_x, neighbour_y = x + diff[i], y + diff[i + 1]
                if 0 <= neighbour_x < m and 0 <= neighbour_y < n and grid[neighbour_x][neighbour_y] != 0:
                    neighbours.append((neighbour_x, neighbour_y))
            if neighbours:
                for neighbour_x, neighbour_y in neighbours:
                    dfs(neighbour_x, neighbour_y, curr_sum)
            else:
                ans = max(ans, curr_sum)

            grid[x][y] = curr_gold

        for x in range(m):
            for y in range(n):
                if grid[x][y] != 0:
                    c = 0
                    for i in range(4):
                        neighbour_x, neighbour_y = x + diff[i], y + diff[i + 1]
                        if 0 <= neighbour_x < m and 0 <= neighbour_y < n and grid[neighbour_x][neighbour_y] != 0:
                            c += 1
                    if c < 3:
                        dfs(x, y, 0)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
