# -*- coding: utf-8 -*-
# LeetCode 3623-统计梯形的数目I

"""
Created on Mon Dec 2 22:12 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        num_parallel = {}
        for _, y in points:
            num_parallel[y] = num_parallel.get(y, 0) + 1
        ans, total_sum = 0, 0
        mod = 10 ** 9 + 7
        for v in num_parallel.values():
            edges = v * (v - 1) // 2
            ans = (ans + edges * total_sum) % mod
            total_sum = (total_sum + edges) % mod
        return ans
