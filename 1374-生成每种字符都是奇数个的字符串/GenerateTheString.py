# -*- coding: utf-8 -*-
# LeetCode 1374-生成每种字符都是奇数个的字符串

"""
Created on Mon Aug 1 09:39 2022

@author: _Mumu
Environment: py38
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n & 1:
            return 'a' * n
        return 'a' + 'b' * (n - 1)
