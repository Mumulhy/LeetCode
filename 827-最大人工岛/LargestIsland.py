# -*- coding: utf-8 -*-
# LeetCode 827-最大人工岛

"""
Created on Sun Sept 18 20:15 2022

@author: _Mumu
Environment: py38
"""

from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[False] * n for _ in range(n)]

        def is_inside(x, y):
            return 0 <= x < n and 0 <= y < n

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        blacks = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    blacks.add((i, j))
        if not blacks:
            return min(n * n, 1)

        unions = []
        while blacks:
            stack = {blacks.pop()}
            union = set()
            edge = set()
            while stack:
                union |= stack
                new_stack = set()
                for point_x, point_y in stack:
                    for dir_x, dir_y in directions:
                        neighbour_x, neighbour_y = point_x + dir_x, point_y + dir_y
                        if is_inside(neighbour_x, neighbour_y) and vis[neighbour_x][neighbour_y] is False:
                            if grid[neighbour_x][neighbour_y] == 1:
                                vis[neighbour_x][neighbour_y] = True
                                new_stack.add((neighbour_x, neighbour_y))
                            else:
                                edge.add((neighbour_x, neighbour_y))
                stack = new_stack
            u = len(union)
            blacks -= union
            unions.append((u, edge))

        edge_to_union = defaultdict(int)
        for u, edge in unions:
            for e in edge:
                edge_to_union[e] += u

        return max(edge_to_union.values()) + 1 if edge_to_union else unions[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.largestIsland([[1, 1], [1, 1]]))
