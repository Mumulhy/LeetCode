# -*- coding: utf-8 -*-
# LeetCode 743-网络延迟时间

"""
Created on Mon Aug 2 20:19 2021

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacency_matrix = [[float('inf')] * n for _ in range(n)]
        for x, y, delay_time in times:
            adjacency_matrix[x - 1][y - 1] = delay_time
        min_delay_time = [float('inf')] * n
        min_delay_time[k - 1] = 0
        uses = [False] * n
        for _ in range(n):
            x = -1
            for y, use in enumerate(uses):
                if not use and (x == -1 or min_delay_time[y] < min_delay_time[x]):
                    x = y
            uses[x] = True
            for y, delay_time in enumerate(adjacency_matrix[x]):
                min_delay_time[y] = min(min_delay_time[y], min_delay_time[x] + delay_time)
        net_delay_time = max(min_delay_time)
        if net_delay_time < float('inf'):
            return net_delay_time
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2))
