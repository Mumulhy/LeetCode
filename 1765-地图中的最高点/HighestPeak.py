# -*- coding: utf-8 -*-
# LeetCode 1765-地图中的最高点

"""
Created on Sat Jan 29 11:38 2022

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        stack = set()
        for x in range(m):
            for y in range(n):
                if isWater[x][y] == 1:
                    visited[x][y] = True
                    stack.add((x, y))
        diff = [-1, 0, 1, 0, -1]
        h = 1
        new_stack = set()
        while stack:
            new_stack.clear()
            for x, y in stack:
                for i in range(4):
                    neighbour_x, neighbour_y = x + diff[i], y + diff[i + 1]
                    if 0 <= neighbour_x < m and 0 <= neighbour_y < n and not visited[neighbour_x][neighbour_y]:
                        height[neighbour_x][neighbour_y] = h
                        visited[neighbour_x][neighbour_y] = True
                        new_stack.add((neighbour_x, neighbour_y))
            h += 1
            stack.clear()
            stack |= new_stack
        return height


if __name__ == '__main__':
    s = Solution()
    for line in s.highestPeak([[0, 0, 1], [1, 0, 0], [0, 0, 0]]):
        print(line)
