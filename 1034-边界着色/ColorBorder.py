# -*- coding: utf-8 -*-
# LeetCode 1034-边界着色

"""
Created on Tues Dec 7 15:01 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        origin_color = grid[row][col]
        visited = [[False] * n for _ in range(m)]
        stack = {(row, col)}
        visited[row][col] = True
        while True:
            new_stack = set()
            for x, y in stack:
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    new_stack.add((x, y))
                elif (grid[x - 1][y] != origin_color or grid[x + 1][y] != origin_color or
                      grid[x][y - 1] != origin_color or grid[x][y + 1] != origin_color):
                    new_stack.add((x, y))
                if x > 0 and grid[x - 1][y] == origin_color and not visited[x - 1][y]:
                    new_stack.add((x - 1, y))
                    visited[x - 1][y] = True
                if x < m - 1 and grid[x + 1][y] == origin_color and not visited[x + 1][y]:
                    new_stack.add((x + 1, y))
                    visited[x + 1][y] = True
                if y > 0 and grid[x][y - 1] == origin_color and not visited[x][y - 1]:
                    new_stack.add((x, y - 1))
                    visited[x][y - 1] = True
                if y < n - 1 and grid[x][y + 1] == origin_color and not visited[x][y + 1]:
                    new_stack.add((x, y + 1))
                    visited[x][y + 1] = True
            if new_stack == stack:
                break
            stack = new_stack
        for x, y in stack:
            grid[x][y] = color
        return grid


if __name__ == '__main__':
    s = Solution()
    print(s.colorBorder(grid=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], row=1, col=1, color=2))
