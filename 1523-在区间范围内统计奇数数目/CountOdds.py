# -*- coding: utf-8 -*-
# LeetCode 1523-在区间范围内统计奇数数目

"""
Created on Sun Dec 7 22:11 2025

@author: _Mumu
Environment: py38
"""


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + ((low % 2) or (high % 2))
