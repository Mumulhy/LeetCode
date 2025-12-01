# -*- coding: utf-8 -*-
# LeetCode 2141-同时运行N台电脑的最长时间

"""
Created on Mon Dec 1 21:44 2025

@author: _Mumu
Environment: py38
"""

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        s = sum(batteries)
        for b in sorted(batteries, reverse=True):
            if b <= s // n:
                return s // n
            s -= b
            n -= 1
