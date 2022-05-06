# -*- coding: utf-8 -*-
# LeetCode 933-最近的请求次数

"""
Created on Fri May 6 09:42 2022

@author: _Mumu
Environment: py38
"""

from bisect import bisect_left


class RecentCounter:
    def __init__(self):
        self.reqs = []

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        idx = bisect_left(self.reqs, t - 3000)
        self.reqs = self.reqs[idx:]
        return len(self.reqs)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
