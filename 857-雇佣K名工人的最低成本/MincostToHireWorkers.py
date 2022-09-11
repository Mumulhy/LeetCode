# -*- coding: utf-8 -*-
# LeetCode 857-雇佣K名工人的最低成本

"""
Created on Sun Sept 11 14:17 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappush, heappop
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        ans = float('inf')
        totalq = 0
        h = []
        for q, w in pairs[:k - 1]:
            totalq += q
            heappush(h, -q)
        for q, w in pairs[k - 1:]:
            totalq += q
            heappush(h, -q)
            ans = min(ans, w / q * totalq)
            totalq += heappop(h)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], k=3))
