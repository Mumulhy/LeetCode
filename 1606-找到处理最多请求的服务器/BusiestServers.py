# -*- coding: utf-8 -*-
# LeetCode 1606-找到处理最多请求的服务器

"""
Created on Wed Mar 30 10:19 2022

@author: _Mumu
Environment: py38
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        reqs = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                _, idx = heappop(busy)
                heappush(available, i + (idx - i) % k)
            if available:
                idx = heappop(available) % k
                reqs[idx] += 1
                heappush(busy, (start + t, idx))
        max_reqs = max(reqs)
        return [i for i, req in enumerate(reqs) if req == max_reqs]


if __name__ == '__main__':
    s = Solution()
    print(s.busiestServers(k=3, arrival=[1, 2, 3], load=[10, 12, 11]))
