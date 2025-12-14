# -*- coding: utf-8 -*-
# LeetCode 2147-分隔长廊的方案数

"""
Created on Sun Dec 14 16:48 2025

@author: _Mumu
Environment: py38
"""


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n = corridor.count('S')
        if n & 1 or n == 0:
            return 0
        mod = 10 ** 9 + 7
        ps = corridor.split('S')[::2]
        ps = list(map(len, ps[1:len(ps) - 1]))
        ans = 1
        for p in ps:
            ans = ans * (p + 1) % mod
        return ans
