# -*- coding: utf-8 -*-
# LeetCode 926-将字符串翻转到单调递增

"""
Created on Sat Jun 11 14:44 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for c in s:
            dp0_new, dp1_new = dp0, min(dp0, dp1)
            if c == '1':
                dp0_new += 1
            else:
                dp1_new += 1
            dp0, dp1 = dp0_new, dp1_new
        return min(dp0, dp1)
