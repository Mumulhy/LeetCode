# -*- coding: utf-8 -*-
# LeetCode 1020-飞地的数量

"""
Created on Sat Feb 12 12:44 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        points, edge = set(), set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    points.add((x, y))
                    if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                        edge.add((x, y))
        if not edge:
            return len(points)
        escape = edge.copy()
        stack, new_stack, visited = set(), set(), set()
        diff = [-1, 0, 1, 0, -1]
        for x, y in edge:
            stack.add((x, y))
            while stack:
                visited |= stack
                for sx, sy in stack:
                    for i in range(4):
                        neighbour_x, neighbour_y = sx + diff[i], sy + diff[i + 1]
                        if 0 <= neighbour_x < m and 0 <= neighbour_y < n and grid[neighbour_x][neighbour_y] == 1:
                            new_stack.add((neighbour_x, neighbour_y))
                stack = new_stack - visited - escape
                new_stack.clear()
            escape |= visited
            visited.clear()
            stack.clear()
        return len(points) - len(escape)


if __name__ == '__main__':
    s = Solution()
    print(s.numEnclaves([[0, 1, 1, 0, 1],
                         [0, 1, 0, 1, 1],
                         [0, 0, 1, 0, 1],
                         [0, 1, 0, 1, 1],
                         [0, 0, 0, 0, 1]]))
