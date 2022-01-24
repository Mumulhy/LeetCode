# -*- coding: utf-8 -*-
# LeetCode 2045-到达目的地的第二短时间

"""
Created on Mon Jan 24 20:20 2022

@author: _Mumu
Environment: py38
"""

from collections import deque
from typing import List


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        while dist[n][1] == float('inf'):
            p = q.popleft()
            for y in graph[p[0]]:
                d = p[1] + 1
                if d < dist[y][0]:
                    dist[y][0] = d
                    q.append((y, d))
                elif dist[y][0] < d < dist[y][1]:
                    dist[y][1] = d
                    q.append((y, d))

        ans = 0
        for _ in range(dist[n][1]):
            if ans % (change * 2) >= change:
                ans += change * 2 - ans % (change * 2)
            ans += time
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.secondMinimum(n=5, edges=[[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], time=3, change=5))
