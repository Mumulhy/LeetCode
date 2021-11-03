# -*- coding: utf-8 -*-
# LeetCode 407-接雨水II

"""
Created on Wed Nov 3 22:35 2021

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        edges = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    visited[i][j] = True
                    heappush(edges, (heightMap[i][j], i * n + j))

        ans = 0
        dirs = [-1, 0, 1, 0, -1]
        while edges:
            height, position = heappop(edges)
            for k in range(4):
                i, j = position // n + dirs[k], position % n + dirs[k + 1]
                if 0 < i < m - 1 and 0 < j < n - 1 and not visited[i][j]:
                    if height > heightMap[i][j]:
                        ans += height - heightMap[i][j]
                    visited[i][j] = True
                    heappush(edges, (max(height, heightMap[i][j]), i * n + j))
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trapRainWater([[12, 13, 1, 12],
                           [13, 4, 13, 12],
                           [13, 8, 10, 12],
                           [12, 13, 12, 12],
                           [13, 13, 13, 13]]))
